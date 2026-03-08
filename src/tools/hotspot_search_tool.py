"""
热点新闻搜索工具
整合了热点新闻检索和历史案例搜索功能
"""

from langchain.tools import tool, ToolRuntime
from coze_coding_dev_sdk import SearchClient
from coze_coding_utils.runtime_ctx.context import new_context
from typing import Optional
import json


@tool
def search_hotspot_news(
    query: str,
    time_range: str = "1d",
    count: int = 10,
    sites: Optional[str] = None,
    runtime: ToolRuntime = None
) -> str:
    """
    搜索过去24小时内的热点新闻（以官方渠道为主）
    
    参数:
        query: 搜索关键词，如"今日热点新闻"、"社会热点"、"政策热点"等
        time_range: 时间范围，默认"1d"（过去1天），支持"1d"、"1w"、"1m"
        count: 返回结果数量，默认10条
        sites: 指定搜索的网站，用逗号分隔，如"people.com.cn,xinhuanet.com,cctv.com"
    
    返回:
        JSON格式的搜索结果，包含标题、摘要、来源、URL等信息
    """
    ctx = runtime.context if runtime else new_context(method="search.hotspot_news")
    
    # 默认搜索官方媒体渠道
    if not sites:
        sites = "people.com.cn,xinhuanet.com,cctv.com,news.cn,chinanews.com,thepaper.cn,caixin.com,finance.sina.com.cn"
    
    client = SearchClient(ctx=ctx)
    
    try:
        response = client.search(
            query=query,
            search_type="web",
            count=count,
            need_content=True,
            need_url=True,
            need_summary=True,
            time_range=time_range,
            sites=sites
        )
        
        results = []
        if response.web_items:
            for item in response.web_items:
                results.append({
                    "title": item.title,
                    "source": item.site_name,
                    "url": item.url,
                    "snippet": item.snippet,
                    "content": item.content[:500] if item.content else "",
                    "publish_time": item.publish_time,
                    "auth_level": item.auth_info_level,
                    "auth_desc": item.auth_info_des
                })
        
        output = {
            "query": query,
            "time_range": time_range,
            "total": len(results),
            "results": results
        }
        
        if response.summary:
            output["ai_summary"] = response.summary
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "query": query
        }, ensure_ascii=False)


@tool
def search_historical_cases(
    topic: str,
    count: int = 5,
    runtime: ToolRuntime = None
) -> str:
    """
    搜索历史类似事件或案例，用于构建案例库
    
    参数:
        topic: 主题关键词，如"房价调控历史"、"养老金改革案例"、"教育政策变化"等
        count: 返回结果数量，默认5条
    
    返回:
        JSON格式的历史案例信息
    """
    ctx = runtime.context if runtime else new_context(method="search.historical_cases")
    
    client = SearchClient(ctx=ctx)
    
    # 构建历史搜索查询
    historical_query = f"{topic} 历史 案例 过往经历"
    
    try:
        response = client.search(
            query=historical_query,
            search_type="web",
            count=count,
            need_content=True,
            need_url=True,
            need_summary=True
        )
        
        results = []
        if response.web_items:
            for item in response.web_items:
                results.append({
                    "title": item.title,
                    "source": item.site_name,
                    "url": item.url,
                    "snippet": item.snippet,
                    "content": item.content[:800] if item.content else "",
                    "publish_time": item.publish_time
                })
        
        output = {
            "topic": topic,
            "total": len(results),
            "historical_cases": results
        }
        
        if response.summary:
            output["ai_summary"] = response.summary
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "topic": topic
        }, ensure_ascii=False)


@tool
def search_comprehensive_hotspots(
    count: int = 15,
    runtime: ToolRuntime = None
) -> str:
    """
    全面检索过去24小时内的重大热点事件（综合多个信息源）
    
    参数:
        count: 每个类别返回的结果数量，默认15条
    
    返回:
        JSON格式的综合热点信息，按类别分类
    """
    ctx = runtime.context if runtime else new_context(method="search.comprehensive_hotspots")
    
    client = SearchClient(ctx=ctx)
    
    # 定义热点类别和对应的搜索关键词
    categories = {
        "社会民生": "民生热点 社会新闻",
        "经济财经": "经济热点 财经新闻",
        "政策法规": "政策热点 新政策",
        "科技动态": "科技热点 创新突破",
        "国际新闻": "国际热点 世界新闻"
    }
    
    all_results = {}
    
    for category, keywords in categories.items():
        try:
            response = client.search(
                query=keywords,
                search_type="web",
                count=count,
                need_content=False,
                need_url=True,
                need_summary=True,
                time_range="1d"
            )
            
            category_results = []
            if response.web_items:
                for item in response.web_items:
                    category_results.append({
                        "title": item.title,
                        "source": item.site_name,
                        "url": item.url,
                        "snippet": item.snippet,
                        "publish_time": item.publish_time
                    })
            
            all_results[category] = category_results
        
        except Exception as e:
            all_results[category] = {"error": str(e)}
    
    output = {
        "timestamp": "past_24_hours",
        "categories": all_results
    }
    
    return json.dumps(output, ensure_ascii=False, indent=2)
