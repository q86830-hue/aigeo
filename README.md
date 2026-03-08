# AIGEO - 白帽GEO内容可信度评估框架

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **让优质内容被AI理解并信任，让污染无处遁形**

AIGEO 是一款白帽GEO（生成式引擎优化）内容可信度评估框架，帮助内容创作者通过真实、可信、结构化的内容，在生成式AI答案中获得优先推荐，同时通过治理污染信源，维护健康的AI信息生态。

## 🌟 核心特性

- **🔍 AI生成检测** - 分析困惑度、突发性，识别AI生成痕迹
- **✅ 事实核查** - 匹配权威数据库，标记无来源或冲突项
- **👤 人类参与度评估** - 评估个人视角、独特经验、具体案例
- **📊 可信度综合评分** - 0-100分综合评分，给出优化建议
- **🏷️ AI友好度增强** - 自动生成Schema.org结构化标记

## 🚀 快速开始

### 安装

```bash
pip install -r requirements.txt
```

### 基本使用

```python
# 使用AIGEO评估内容可信度
from src.agents.standalone_agent import build_agent

# 构建评估Agent
agent = build_agent()

# 评估内容
result = agent.assess("你的文章内容...")

print(f"可信度评分: {result.score}/100")
print(f"AI生成概率: {result.ai_probability}")
print(f"事实核查: {result.fact_check_results}")
```

## 📖 文档

- [快速开始指南](STANDALONE_GUIDE.md) - 独立版使用指南
- [AIGEO优化提示词](PROMPT_AIGEO_OPTIMIZED.md) - 内容创作提示词
- [内容评估报告](content_audit_report.md) - 评估标准示例
- [产品规划书](GITHUB_PUBLISH_GUIDE.md) - 完整产品规划

## 🏗️ 项目结构

```
WZSPG/
├── config/                     # 配置文件
│   ├── standalone_config.json  # AIGEO优化版配置
│   └── agent_llm_config.json   # 原始配置
├── src/                        # 源代码
│   ├── agents/                 # Agent实现
│   │   ├── standalone_agent.py # AIGEO评估Agent
│   │   └── agent.py            # 原始Agent
│   ├── tools/                  # 工具集
│   │   ├── standalone_tools.py # 独立版工具
│   │   └── ...
│   └── main.py                 # 主入口
├── .trae/skills/               # Trae Skills
│   └── aigeo-product-planner/  # AIGEO产品规划Skill
├── docs/                       # 文档
│   ├── STANDALONE_GUIDE.md
│   ├── PROMPT_AIGEO_OPTIMIZED.md
│   ├── content_audit_report.md
│   └── GITHUB_PUBLISH_GUIDE.md
├── LICENSE                     # MIT许可证
├── README.md                   # 本文件
└── requirements.txt            # 依赖列表
```

## 🎯 核心模块

### 1. 内容可信度评估引擎
- **AI生成检测**: 分析困惑度、突发性
- **原创性检测**: 与权威内容相似度比对
- **事实核查**: 匹配权威数据库
- **人类参与度评估**: 个人视角、独特经验
- **可信度综合评分**: 0-100分

### 2. AI友好度增强引擎
- **结构化标记生成**: Schema.org JSON-LD
- **关键信息抽取**: 5W1H提取
- **AI友好度评分**: 标题、结构、信息密度

### 3. 信源网络构建引擎
- **权威信源数据库**: 动态更新的高质量域名库
- **引用关系图谱**: 可视化内容引用关系
- **虚假网络检测**: 识别低质链接农场

## 🤝 贡献

我们欢迎所有形式的贡献！请查看以下内容了解如何参与：

- [贡献指南](GITHUB_PUBLISH_GUIDE.md#贡献指南)
- [行为准则](GITHUB_PUBLISH_GUIDE.md#行为准则)

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🙏 致谢

感谢所有为AIGEO做出贡献的开发者！

---

**AIGEO** - 白帽GEO内容可信度评估框架  
让优质内容被AI理解并信任，让污染无处遁形
