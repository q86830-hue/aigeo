"""
热点新闻口述稿生成Agent
主逻辑文件
"""

import os
import json
from typing import Annotated
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from coze_coding_utils.runtime_ctx.context import default_headers
from storage.memory.memory_saver import get_memory_saver
from tools.hotspot_search_tool import (
    search_hotspot_news,
    search_historical_cases,
    search_comprehensive_hotspots
)
from tools.document_export_tool import (
    export_to_txt,
    export_to_word,
    export_document
)

# 配置文件路径
LLM_CONFIG = "config/agent_llm_config.json"

# 默认保留最近20轮对话（40条消息）
MAX_MESSAGES = 40


def _windowed_messages(old, new):
    """滑动窗口：只保留最近MAX_MESSAGES条消息"""
    # 调用原始的 add_messages reducer
    merged = add_messages(old, new)
    # 转换为列表并应用滑动窗口
    messages_list = list(merged) if not isinstance(merged, list) else merged
    return messages_list[-MAX_MESSAGES:]  # type: ignore


class AgentState(MessagesState):
    """Agent状态，包含消息历史"""
    messages: Annotated[list[AnyMessage], _windowed_messages]


def build_agent(ctx=None):
    """
    构建并返回热点新闻口述稿生成Agent
    
    参数:
        ctx: 运行时上下文，用于请求追踪
    
    返回:
        Agent实例
    """
    # 获取工作目录
    workspace_path = os.getenv("COZE_WORKSPACE_PATH", "/workspace/projects")
    config_path = os.path.join(workspace_path, LLM_CONFIG)
    
    # 读取配置文件
    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    
    # 获取API密钥和基础URL
    api_key = os.getenv("COZE_WORKLOAD_IDENTITY_API_KEY")
    base_url = os.getenv("COZE_INTEGRATION_MODEL_BASE_URL")
    
    # 初始化LLM
    llm = ChatOpenAI(
        model=cfg['config'].get("model"),
        api_key=api_key,
        base_url=base_url,
        temperature=cfg['config'].get('temperature', 0.8),
        streaming=True,
        timeout=cfg['config'].get('timeout', 600),
        extra_body={
            "thinking": {
                "type": cfg['config'].get('thinking', 'enabled')
            }
        },
        default_headers=default_headers(ctx) if ctx else {}
    )
    
    # 注册工具
    tools = [
        search_hotspot_news,
        search_historical_cases,
        search_comprehensive_hotspots,
        export_to_txt,
        export_to_word,
        export_document
    ]
    
    # 创建Agent
    agent = create_agent(
        model=llm,
        system_prompt=cfg.get("sp"),
        tools=tools,
        checkpointer=get_memory_saver(),
        state_schema=AgentState,
    )
    
    return agent
