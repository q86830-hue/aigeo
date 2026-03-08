"""
独立版工具集 - 无Coze平台依赖
使用标准HTTP请求实现搜索和文档导出功能
"""

import os
import json
import httpx
from typing import Optional
from langchain.tools import tool
from datetime import datetime


def _get_search_api_key() -> Optional[str]:
    """获取搜索API密钥"""
    return os.getenv("SEARCH_API_KEY") or os.getenv("SERPER_API_KEY") or os.getenv("GOOGLE_API_KEY")


def _get_search_engine_id() -> Optional[str]:
    """获取搜索引擎ID"""
    return os.getenv("SEARCH_ENGINE_ID") or os.getenv("GOOGLE_CX")


@tool
def search_hotspot_news(
    query: str,
    time_range: str = "1d",
    count: int = 10,
    sites: Optional[str] = None
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
    api_key = _get_search_api_key()
    
    if not api_key:
        return json.dumps({
            "error": "请设置 SEARCH_API_KEY 或 SERPER_API_KEY 环境变量",
            "query": query
        }, ensure_ascii=False)
    
    if not sites:
        sites = "people.com.cn,xinhuanet.com,cctv.com,news.cn,chinanews.com,thepaper.cn,caixin.com"
    
    site_filter = " OR ".join([f"site:{s.strip()}" for s in sites.split(",")])
    full_query = f"{query} {site_filter}"
    
    serper_url = "https://google.serper.dev/search"
    
    try:
        with httpx.Client(timeout=30) as client:
            response = client.post(
                serper_url,
                headers={
                    "X-API-KEY": api_key,
                    "Content-Type": "application/json"
                },
                json={
                    "q": full_query,
                    "num": count,
                    "tbs": f"qdr:{time_range.replace('1d', 'd').replace('1w', 'w').replace('1m', 'm')}"
                }
            )
            response.raise_for_status()
            data = response.json()
        
        results = []
        for item in data.get("organic", [])[:count]:
            results.append({
                "title": item.get("title", ""),
                "source": item.get("displayLink", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
                "publish_time": item.get("date", "")
            })
        
        output = {
            "query": query,
            "time_range": time_range,
            "total": len(results),
            "results": results
        }
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "query": query
        }, ensure_ascii=False)


@tool
def search_historical_cases(
    topic: str,
    count: int = 5
) -> str:
    """
    搜索历史类似事件或案例，用于构建案例库
    
    参数:
        topic: 主题关键词，如"房价调控历史"、"养老金改革案例"、"教育政策变化"等
        count: 返回结果数量，默认5条
    
    返回:
        JSON格式的历史案例信息
    """
    api_key = _get_search_api_key()
    
    if not api_key:
        return json.dumps({
            "error": "请设置 SEARCH_API_KEY 或 SERPER_API_KEY 环境变量",
            "topic": topic
        }, ensure_ascii=False)
    
    historical_query = f"{topic} 历史 案例 过往经历"
    
    serper_url = "https://google.serper.dev/search"
    
    try:
        with httpx.Client(timeout=30) as client:
            response = client.post(
                serper_url,
                headers={
                    "X-API-KEY": api_key,
                    "Content-Type": "application/json"
                },
                json={
                    "q": historical_query,
                    "num": count
                }
            )
            response.raise_for_status()
            data = response.json()
        
        results = []
        for item in data.get("organic", [])[:count]:
            results.append({
                "title": item.get("title", ""),
                "source": item.get("displayLink", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
                "publish_time": item.get("date", "")
            })
        
        output = {
            "topic": topic,
            "total": len(results),
            "historical_cases": results
        }
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "topic": topic
        }, ensure_ascii=False)


@tool
def search_comprehensive_hotspots(
    count: int = 15
) -> str:
    """
    全面检索过去24小时内的重大热点事件（综合多个信息源）
    
    参数:
        count: 每个类别返回的结果数量，默认15条
    
    返回:
        JSON格式的综合热点信息，按类别分类
    """
    api_key = _get_search_api_key()
    
    if not api_key:
        return json.dumps({
            "error": "请设置 SEARCH_API_KEY 或 SERPER_API_KEY 环境变量"
        }, ensure_ascii=False)
    
    categories = {
        "社会民生": "民生热点 社会新闻",
        "经济财经": "经济热点 财经新闻",
        "政策法规": "政策热点 新政策",
        "科技动态": "科技热点 创新突破",
        "国际新闻": "国际热点 世界新闻"
    }
    
    all_results = {}
    serper_url = "https://google.serper.dev/search"
    
    with httpx.Client(timeout=30) as client:
        for category, keywords in categories.items():
            try:
                response = client.post(
                    serper_url,
                    headers={
                        "X-API-KEY": api_key,
                        "Content-Type": "application/json"
                    },
                    json={
                        "q": keywords,
                        "num": count,
                        "tbs": "qdr:d"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                category_results = []
                for item in data.get("organic", [])[:count]:
                    category_results.append({
                        "title": item.get("title", ""),
                        "source": item.get("displayLink", ""),
                        "url": item.get("link", ""),
                        "snippet": item.get("snippet", ""),
                        "publish_time": item.get("date", "")
                    })
                
                all_results[category] = category_results
            
            except Exception as e:
                all_results[category] = {"error": str(e)}
    
    output = {
        "timestamp": "past_24_hours",
        "categories": all_results
    }
    
    return json.dumps(output, ensure_ascii=False, indent=2)


@tool
def export_to_txt(
    content: str,
    filename: str = "口述稿"
) -> str:
    """
    将口述稿内容导出为TXT文本文件
    
    参数:
        content: 口述稿的文本内容
        filename: 文件名（不含扩展名）
    
    返回:
        导出结果信息
    """
    try:
        output_dir = os.getenv("OUTPUT_DIR", "./output")
        os.makedirs(output_dir, exist_ok=True)
        
        safe_filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_filename = f"{safe_filename}_{timestamp}.txt"
        filepath = os.path.join(output_dir, full_filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return json.dumps({
            "success": True,
            "format": "TXT",
            "filename": full_filename,
            "filepath": filepath,
            "message": f"文档已成功导出为TXT格式，保存至: {filepath}"
        }, ensure_ascii=False)
    
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e),
            "message": "导出失败，请重试"
        }, ensure_ascii=False)


@tool
def export_to_word(
    content: str,
    filename: str = "口述稿"
) -> str:
    """
    将口述稿内容导出为Word文档（DOCX格式）
    
    参数:
        content: 口述稿的文本内容（支持Markdown格式）
        filename: 文件名（不含扩展名）
    
    返回:
        导出结果信息
    """
    try:
        from docx import Document
        from docx.shared import Pt, Inches
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        
        output_dir = os.getenv("OUTPUT_DIR", "./output")
        os.makedirs(output_dir, exist_ok=True)
        
        safe_filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_filename = f"{safe_filename}_{timestamp}.docx"
        filepath = os.path.join(output_dir, full_filename)
        
        doc = Document()
        
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Microsoft YaHei'
        font.size = Pt(12)
        
        paragraphs = content.split('\n')
        for para_text in paragraphs:
            if para_text.strip():
                p = doc.add_paragraph(para_text)
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        doc.save(filepath)
        
        return json.dumps({
            "success": True,
            "format": "DOCX",
            "filename": full_filename,
            "filepath": filepath,
            "message": f"文档已成功导出为Word格式，保存至: {filepath}"
        }, ensure_ascii=False)
    
    except ImportError:
        return json.dumps({
            "success": False,
            "error": "python-docx 库未安装，请运行: pip install python-docx",
            "message": "导出失败"
        }, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e),
            "message": "导出失败，请重试"
        }, ensure_ascii=False)


@tool
def export_document(
    content: str,
    filename: str = "口述稿",
    format_type: str = "word"
) -> str:
    """
    导出口述稿文档（支持TXT和Word格式）
    
    参数:
        content: 口述稿的文本内容
        filename: 文件名（不含扩展名）
        format_type: 格式类型，"txt" 或 "word"
    
    返回:
        文档导出信息
    """
    if format_type.lower() == "txt":
        return export_to_txt(content, filename)
    elif format_type.lower() in ["word", "docx"]:
        return export_to_word(content, filename)
    else:
        return json.dumps({
            "success": False,
            "error": f"不支持的格式: {format_type}",
            "message": "请选择 'txt' 或 'word' 格式"
        }, ensure_ascii=False)
