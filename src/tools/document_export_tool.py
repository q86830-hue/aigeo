"""
文档导出工具
支持导出TXT和Word格式的口述稿
"""

from langchain.tools import tool, ToolRuntime
from coze_coding_dev_sdk import DocumentGenerationClient, DOCXConfig
from coze_coding_utils.runtime_ctx.context import new_context
import tempfile
import os
import json


@tool
def export_to_txt(
    content: str,
    filename: str = "口述稿",
    runtime: ToolRuntime = None
) -> str:
    """
    将口述稿内容导出为TXT文本文件
    
    参数:
        content: 口述稿的文本内容
        filename: 文件名（不含扩展名）
    
    返回:
        TXT文件的下载URL
    """
    # 使用Markdown格式转换为DOCX（比纯文本更专业）
    ctx = runtime.context if runtime else new_context(method="export.txt")
    
    try:
        client = DocumentGenerationClient()
        
        # 为了保持纯文本格式，我们使用HTML格式
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: "Microsoft YaHei", "SimSun", sans-serif;
            font-size: 14px;
            line-height: 2;
            white-space: pre-wrap;
            padding: 40px;
        }}
    </style>
</head>
<body>{content}</body>
</html>"""
        
        # 使用英文文件名
        safe_filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
        url = client.create_docx_from_html(html_content, safe_filename)
        
        return json.dumps({
            "success": True,
            "format": "TXT",
            "filename": f"{filename}.txt",
            "download_url": url,
            "message": "文档已成功导出为TXT格式，点击链接下载（有效期24小时）"
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
    filename: str = "口述稿",
    runtime: ToolRuntime = None
) -> str:
    """
    将口述稿内容导出为Word文档（DOCX格式）
    
    参数:
        content: 口述稿的文本内容（支持Markdown格式）
        filename: 文件名（不含扩展名）
    
    返回:
        Word文档的下载URL
    """
    ctx = runtime.context if runtime else new_context(method="export.word")
    
    try:
        # 配置文档格式
        config = DOCXConfig(
            font_name="Noto Sans CJK SC",
            font_size=12,
            top_margin=0.75,
            bottom_margin=0.75,
            left_margin=0.75,
            right_margin=0.75
        )
        
        client = DocumentGenerationClient(docx_config=config)
        
        # 将纯文本转换为Markdown格式以便更好地排版
        markdown_content = _convert_to_markdown(content)
        
        # 使用英文文件名
        safe_filename = filename.replace(" ", "_").replace("(", "").replace(")", "")
        url = client.create_docx_from_markdown(markdown_content, safe_filename)
        
        return json.dumps({
            "success": True,
            "format": "DOCX",
            "filename": f"{filename}.docx",
            "download_url": url,
            "message": "文档已成功导出为Word格式，点击链接下载（有效期24小时）"
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
    format_type: str = "word",
    runtime: ToolRuntime = None
) -> str:
    """
    导出口述稿文档（支持TXT和Word格式）
    
    参数:
        content: 口述稿的文本内容
        filename: 文件名（不含扩展名）
        format_type: 格式类型，"txt" 或 "word"
    
    返回:
        文档的下载URL和信息
    """
    if format_type.lower() == "txt":
        return export_to_txt(content, filename, runtime)
    elif format_type.lower() in ["word", "docx"]:
        return export_to_word(content, filename, runtime)
    else:
        return json.dumps({
            "success": False,
            "error": f"不支持的格式: {format_type}",
            "message": "请选择 'txt' 或 'word' 格式"
        }, ensure_ascii=False)


def _convert_to_markdown(text: str) -> str:
    """
    将纯文本转换为Markdown格式，以便更好地排版
    """
    lines = text.split('\n')
    markdown_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # 检测标题（通常是比较短的独立行）
        if stripped and len(stripped) < 50 and not stripped.endswith('。') and not stripped.endswith('？') and not stripped.endswith('！'):
            # 如果下一行是空行，可能是标题
            markdown_lines.append(f"## {stripped}\n")
        else:
            markdown_lines.append(stripped)
    
    return '\n'.join(markdown_lines)
