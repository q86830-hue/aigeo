"""
独立版主入口 - 无Coze平台依赖
支持 HTTP 服务、命令行运行等多种模式
"""

import argparse
import asyncio
import json
import logging
import os
import sys
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

setup_logging = lambda: logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    import uvicorn
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import StreamingResponse, JSONResponse
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False
    logger.warning("FastAPI not installed, HTTP mode unavailable. Run: pip install fastapi uvicorn")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.standalone_agent import build_agent


class StandaloneService:
    """独立版服务类"""
    
    def __init__(self):
        self._agent = None
    
    def get_agent(self):
        """获取Agent实例（延迟加载）"""
        if self._agent is None:
            self._agent = build_agent()
        return self._agent
    
    async def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """同步运行Agent"""
        agent = self.get_agent()
        config = {"configurable": {"thread_id": payload.get("session_id", "default")}}
        result = await agent.ainvoke(payload, config=config)
        return result
    
    def stream(self, payload: Dict[str, Any]):
        """流式运行Agent"""
        agent = self.get_agent()
        config = {"configurable": {"thread_id": payload.get("session_id", "default")}}
        for chunk in agent.stream(payload, config=config):
            yield chunk


if FASTAPI_AVAILABLE:
    service = StandaloneService()
    app = FastAPI(title="热点新闻口述稿生成Agent", version="1.0.0")
    
    @app.post("/run")
    async def http_run(request: Request) -> Dict[str, Any]:
        """同步运行接口"""
        try:
            payload = await request.json()
            return await service.run(payload)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON format")
        except Exception as e:
            logger.error(f"Error in http_run: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.post("/stream_run")
    async def http_stream_run(request: Request):
        """流式运行接口"""
        try:
            payload = await request.json()
            
            async def generate():
                for chunk in service.stream(payload):
                    yield f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"
            
            return StreamingResponse(generate(), media_type="text/event-stream")
        except Exception as e:
            logger.error(f"Error in http_stream_run: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/health")
    async def health_check():
        """健康检查"""
        return {"status": "ok", "message": "Service is running"}
    
    @app.post("/v1/chat/completions")
    async def openai_chat_completions(request: Request):
        """OpenAI 兼容接口"""
        try:
            payload = await request.json()
            messages = payload.get("messages", [])
            
            agent_payload = {
                "messages": messages
            }
            
            result = await service.run(agent_payload)
            
            return {
                "id": "chatcmpl-standalone",
                "object": "chat.completion",
                "choices": [{
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": result.get("output", str(result))
                    },
                    "finish_reason": "stop"
                }]
            }
        except Exception as e:
            logger.error(f"Error in openai_chat_completions: {e}")
            raise HTTPException(status_code=500, detail=str(e))


def parse_args():
    parser = argparse.ArgumentParser(description="热点新闻口述稿生成Agent - 独立版")
    parser.add_argument("-m", type=str, default="flow", help="运行模式: http, flow, chat")
    parser.add_argument("-p", type=int, default=5000, help="HTTP服务端口")
    parser.add_argument("-i", type=str, default="", help="输入文本或JSON")
    parser.add_argument("-c", type=str, default="", help="配置文件路径")
    return parser.parse_args()


def parse_input(input_str: str) -> Dict[str, Any]:
    """解析输入"""
    if not input_str:
        return {"messages": [{"role": "user", "content": "你好，请介绍一下你自己"}]}
    
    try:
        return json.loads(input_str)
    except json.JSONDecodeError:
        return {"messages": [{"role": "user", "content": input_str}]}


def start_http_server(port: int):
    """启动HTTP服务"""
    if not FASTAPI_AVAILABLE:
        print("错误: FastAPI未安装，无法启动HTTP服务")
        print("请运行: pip install fastapi uvicorn")
        sys.exit(1)
    
    print(f"启动HTTP服务，端口: {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)


async def run_flow(payload: Dict[str, Any]):
    """运行Flow模式"""
    service = StandaloneService()
    result = await service.run(payload)
    return result


def run_chat():
    """交互式聊天模式"""
    print("=" * 50)
    print("热点新闻口述稿生成Agent - 交互模式")
    print("输入 'quit' 或 'exit' 退出")
    print("=" * 50)
    
    service = StandaloneService()
    session_id = "chat_session"
    
    while True:
        try:
            user_input = input("\n用户: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("再见!")
                break
            
            if not user_input:
                continue
            
            payload = {
                "messages": [{"role": "user", "content": user_input}],
                "session_id": session_id
            }
            
            print("\n助手: ", end="", flush=True)
            
            agent = service.get_agent()
            config = {"configurable": {"thread_id": session_id}}
            
            for chunk in agent.stream(payload, config=config):
                if isinstance(chunk, dict):
                    if "output" in chunk:
                        print(chunk["output"], end="", flush=True)
                    elif "messages" in chunk:
                        for msg in chunk["messages"]:
                            if hasattr(msg, "content"):
                                print(msg.content, end="", flush=True)
            
            print()
        
        except KeyboardInterrupt:
            print("\n再见!")
            break
        except Exception as e:
            print(f"\n错误: {e}")


if __name__ == "__main__":
    args = parse_args()
    setup_logging()
    
    if args.m == "http":
        start_http_server(args.p)
    
    elif args.m == "flow":
        payload = parse_input(args.i)
        result = asyncio.run(run_flow(payload))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.m == "chat":
        run_chat()
    
    else:
        print(f"未知模式: {args.m}")
        print("支持的模式: http, flow, chat")
