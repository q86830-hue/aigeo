"""
热点新闻口述稿生成Agent
独立版本 - 无Coze平台依赖
"""

import os
import json
from typing import Annotated, Optional
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from langgraph.checkpoint.memory import MemorySaver
from tools.standalone_tools import (
    search_hotspot_news,
    search_historical_cases,
    search_comprehensive_hotspots,
    export_to_txt,
    export_to_word,
    export_document
)

STANDALONE_CONFIG = "config/standalone_config.json"
MAX_MESSAGES = 40


def _windowed_messages(old, new):
    """滑动窗口：只保留最近MAX_MESSAGES条消息"""
    merged = add_messages(old, new)
    messages_list = list(merged) if not isinstance(merged, list) else merged
    return messages_list[-MAX_MESSAGES:]


class AgentState(MessagesState):
    """Agent状态，包含消息历史"""
    messages: Annotated[list[AnyMessage], _windowed_messages]


def build_agent(ctx=None, config_path: Optional[str] = None):
    """
    构建并返回热点新闻口述稿生成Agent
    
    参数:
        ctx: 运行时上下文（兼容原接口，独立模式下忽略）
        config_path: 配置文件路径（可选）
    
    返回:
        Agent实例
    """
    workspace_path = os.getenv("WORKSPACE_PATH", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    if config_path is None:
        config_path = os.path.join(workspace_path, STANDALONE_CONFIG)
    
    if not os.path.exists(config_path):
        config_path = os.path.join(workspace_path, "config", "standalone_config.json")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    
    api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("API_BASE_URL") or cfg.get("api", {}).get("base_url", "https://api.deepseek.com")
    
    if not api_key:
        raise ValueError("请设置环境变量 DEEPSEEK_API_KEY 或 OPENAI_API_KEY")
    
    llm = ChatOpenAI(
        model=cfg['config'].get("model", "deepseek-chat"),
        api_key=api_key,
        base_url=base_url,
        temperature=cfg['config'].get('temperature', 0.72),
        streaming=True,
        timeout=cfg['config'].get('timeout', 600),
        max_tokens=cfg['config'].get('max_tokens', 8000),
    )
    
    tools = [
        search_hotspot_news,
        search_historical_cases,
        search_comprehensive_hotspots,
        export_to_txt,
        export_to_word,
        export_document
    ]
    
    agent = create_agent(
        model=llm,
        system_prompt=cfg.get("sp"),
        tools=tools,
        checkpointer=MemorySaver(),
        state_schema=AgentState,
    )
    
    return agent


def build_agent_with_custom_llm(llm, system_prompt: Optional[str] = None, config_path: Optional[str] = None):
    """
    使用自定义LLM构建Agent
    
    参数:
        llm: LangChain兼容的LLM实例
        system_prompt: 自定义系统提示词（可选）
        config_path: 配置文件路径（用于获取默认提示词）
    
    返回:
        Agent实例
    """
    if system_prompt is None:
        workspace_path = os.getenv("WORKSPACE_PATH", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if config_path is None:
            config_path = os.path.join(workspace_path, STANDALONE_CONFIG)
        
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        system_prompt = cfg.get("sp")
    
    tools = [
        search_hotspot_news,
        search_historical_cases,
        search_comprehensive_hotspots,
        export_to_txt,
        export_to_word,
        export_document
    ]
    
    agent = create_agent(
        model=llm,
        system_prompt=system_prompt,
        tools=tools,
        checkpointer=MemorySaver(),
        state_schema=AgentState,
    )
    
    return agent
