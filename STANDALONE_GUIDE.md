# 热点新闻口述稿生成Agent - 独立版使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.standalone.txt
```

### 2. 配置环境变量

复制 `.env.template` 为 `.env` 并填入API密钥：

```bash
cp .env.template .env
```

编辑 `.env` 文件：

```env
# 必填: LLM API密钥
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# 可选: 搜索API (用于热点搜索工具)
SERPER_API_KEY=your_serper_api_key_here
```

### 3. 运行

**Windows:**
```batch
scripts\standalone_run.bat chat
```

**或直接运行Python:**
```bash
cd src
python standalone_main.py -m chat
```

## 运行模式

### HTTP服务模式
```bash
# 默认端口5000
python standalone_main.py -m http

# 指定端口
python standalone_main.py -m http -p 8080
```

**API接口:**
- `POST /run` - 同步运行
- `POST /stream_run` - 流式运行
- `POST /v1/chat/completions` - OpenAI兼容接口
- `GET /health` - 健康检查

### 单次运行模式
```bash
python standalone_main.py -m flow -i "请写一篇关于AI的热点口述稿"
```

### 交互式聊天模式
```bash
python standalone_main.py -m chat
```

## 配置说明

### LLM配置 (config/standalone_config.json)

| 参数 | 说明 | 默认值 |
|------|------|--------|
| model | 模型名称 | deepseek-chat |
| temperature | 温度参数 | 0.72 |
| max_tokens | 最大输出token | 8000 |

### 支持的LLM

- **DeepSeek** (推荐): 设置 `DEEPSEEK_API_KEY`
- **OpenAI**: 设置 `OPENAI_API_KEY`
- **其他兼容API**: 设置 `API_BASE_URL` 和对应的API密钥

## 工具说明

| 工具 | 功能 | 依赖 |
|------|------|------|
| search_hotspot_news | 搜索热点新闻 | SERPER_API_KEY |
| search_historical_cases | 搜索历史案例 | SERPER_API_KEY |
| search_comprehensive_hotspots | 综合热点检索 | SERPER_API_KEY |
| export_to_txt | 导出TXT文件 | 无 |
| export_to_word | 导出Word文档 | python-docx |

## 代码调用示例

```python
from agents.standalone_agent import build_agent

# 构建Agent
agent = build_agent()

# 运行
result = await agent.ainvoke({
    "messages": [{"role": "user", "content": "请写一篇热点口述稿"}]
})

# 流式运行
for chunk in agent.stream({"messages": [...]}):
    print(chunk)
```

## 文件结构

```
WZSPG/
├── config/
│   ├── agent_llm_config.json    # 原Coze配置
│   └── standalone_config.json   # 独立版配置
├── src/
│   ├── agents/
│   │   ├── agent.py             # 原Agent (Coze依赖)
│   │   └── standalone_agent.py  # 独立版Agent
│   ├── tools/
│   │   ├── hotspot_search_tool.py    # 原工具 (Coze SDK)
│   │   ├── document_export_tool.py   # 原工具 (Coze SDK)
│   │   └── standalone_tools.py       # 独立版工具
│   ├── main.py                  # 原入口
│   └── standalone_main.py       # 独立版入口
├── scripts/
│   └── standalone_run.bat       # Windows启动脚本
├── .env.template                # 环境变量模板
└── requirements.standalone.txt  # 独立版依赖
```

## 与原版对比

| 特性 | 原版 (Coze) | 独立版 |
|------|-------------|--------|
| LLM调用 | Coze平台API | 标准OpenAI API |
| 搜索服务 | Coze SearchClient | Serper/Google API |
| 文档导出 | Coze DocumentClient | 本地文件/python-docx |
| 会话存储 | PostgreSQL/Memory | Memory |
| 身份认证 | Coze Workload Identity | 无 |

## 常见问题

**Q: 搜索工具报错怎么办？**
A: 设置 `SERPER_API_KEY` 环境变量，可从 https://serper.dev 免费获取

**Q: 如何使用其他LLM？**
A: 设置 `API_BASE_URL` 和对应的API密钥，如：
```env
API_BASE_URL=https://api.openai.com/v1
OPENAI_API_KEY=sk-xxx
```

**Q: Word导出失败？**
A: 安装 python-docx: `pip install python-docx`
