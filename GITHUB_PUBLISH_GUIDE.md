# AIGEO GitHub 开源发布指南

本文档指导您将 AIGEO 白帽GEO内容可信度评估框架发布到 GitHub 开源。

---

## 📋 发布前检查清单

### 1. 代码与文档准备
- [ ] 核心代码已完成并测试
- [ ] README.md 编写完成（中英文）
- [ ] LICENSE 文件选择并添加
- [ ] CONTRIBUTING.md 贡献指南
- [ ] CODE_OF_CONDUCT.md 行为准则
- [ ] CHANGELOG.md 更新日志

### 2. 敏感信息清理
- [ ] 删除所有 API 密钥和密码
- [ ] 删除个人身份信息
- [ ] 检查配置文件中的敏感数据
- [ ] 确保 .env 文件在 .gitignore 中

### 3. 项目结构整理
- [ ] 目录结构清晰
- [ ] 不必要的文件已清理
- [ ] 示例文件完整

---

## 🚀 发布步骤

### 步骤 1: 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 "+" → "New repository"
3. 填写仓库信息：
   - **Repository name**: `aigeo` 或 `aigeo-framework`
   - **Description**: 白帽GEO内容可信度评估框架 / White-hat GEO Content Credibility Assessment Framework
   - **Visibility**: Public
   - **Initialize**: 勾选 "Add a README file"
   - **Add .gitignore**: 选择 "Python"（如果是Python项目）
   - **Choose a license**: 选择 "MIT License"（推荐）

### 步骤 2: 本地项目初始化

```bash
# 进入项目目录
cd G:\WZSPG

# 初始化 Git 仓库（如果还没有）
git init

# 添加远程仓库（替换 YOUR_USERNAME 为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/aigeo.git

# 或者使用 SSH
git remote add origin git@github.com:YOUR_USERNAME/aigeo.git
```

### 步骤 3: 配置 .gitignore

创建 `.gitignore` 文件：

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# 虚拟环境
venv/
ENV/
env/
.venv

# 环境变量和敏感信息
.env
.env.local
.env.*.local
*.pem
*.key

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# 操作系统
.DS_Store
Thumbs.db

# 日志
*.log
logs/

# 测试
.pytest_cache/
.coverage
htmlcov/

# 临时文件
tmp/
temp/
*.tmp

# 输出文件（可选）
output/
exports/
```

### 步骤 4: 提交代码

```bash
# 添加所有文件
git add .

# 提交（使用规范化的提交信息）
git commit -m "feat: initial release of AIGEO framework

- Add content credibility assessment engine
- Add AI generation detection module
- Add fact verification system
- Add human contribution scoring
- Add comprehensive documentation"

# 推送到 GitHub
git push -u origin main
```

### 步骤 5: 创建 Release

1. 在 GitHub 仓库页面，点击右侧 "Releases"
2. 点击 "Create a new release"
3. 填写版本信息：
   - **Choose a tag**: `v1.0.0`
   - **Release title**: `AIGEO v1.0.0 - Initial Release`
   - **Describe this release**: 填写更新日志

---

## 📁 必备文件模板

### 1. README.md（中文）

```markdown
# AIGEO - 白帽GEO内容可信度评估框架

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **让优质内容被AI理解并信任，让污染无处遁形**

AIGEO 是一款白帽GEO（生成式引擎优化）内容可信度评估框架，帮助内容创作者通过真实、可信、结构化的内容，在生成式AI答案中获得优先推荐。

## 🌟 核心特性

- **🔍 AI生成检测** - 分析困惑度、突发性，识别AI生成痕迹
- **✅ 事实核查** - 匹配权威数据库，标记无来源或冲突项
- **👤 人类参与度评估** - 评估个人视角、独特经验、具体案例
- **📊 可信度综合评分** - 0-100分综合评分，给出优化建议
- **🏷️ AI友好度增强** - 自动生成Schema.org结构化标记

## 🚀 快速开始

### 安装

```bash
pip install aigeo
```

### 基本使用

```python
from aigeo import CredibilityAssessor

# 初始化评估器
assessor = CredibilityAssessor()

# 评估内容
text = "你的文章内容..."
result = assessor.assess(text)

print(f"可信度评分: {result.score}/100")
print(f"AI生成概率: {result.ai_probability}")
print(f"事实核查: {result.fact_check_results}")
```

## 📖 文档

- [快速开始指南](docs/quickstart.md)
- [API文档](docs/api.md)
- [评估标准](docs/criteria.md)
- [贡献指南](CONTRIBUTING.md)

## 🤝 贡献

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🙏 致谢

感谢所有为AIGEO做出贡献的开发者！

---

**AIGEO** - 白帽GEO内容可信度评估框架  
让优质内容被AI理解并信任
```

### 2. README.md（English）

```markdown
# AIGEO - White-hat GEO Content Credibility Assessment Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **Let quality content be understood and trusted by AI, let pollution have nowhere to hide**

AIGEO is a white-hat GEO (Generative Engine Optimization) content credibility assessment framework that helps content creators gain priority recommendations in generative AI answers through authentic, credible, and structured content.

## 🌟 Core Features

- **🔍 AI Generation Detection** - Analyze perplexity and burstiness to identify AI-generated traces
- **✅ Fact Verification** - Match authoritative databases, flag unsourced or conflicting claims
- **👤 Human Contribution Assessment** - Evaluate personal perspective, unique experience, specific cases
- **📊 Comprehensive Credibility Score** - 0-100 scoring with optimization suggestions
- **🏷️ AI-Friendly Enhancement** - Auto-generate Schema.org structured markup

## 🚀 Quick Start

### Installation

```bash
pip install aigeo
```

### Basic Usage

```python
from aigeo import CredibilityAssessor

# Initialize assessor
assessor = CredibilityAssessor()

# Assess content
text = "Your article content..."
result = assessor.assess(text)

print(f"Credibility Score: {result.score}/100")
print(f"AI Generation Probability: {result.ai_probability}")
print(f"Fact Check: {result.fact_check_results}")
```

## 📖 Documentation

- [Quick Start Guide](docs/quickstart.md)
- [API Documentation](docs/api.md)
- [Assessment Criteria](docs/criteria.md)
- [Contributing Guide](CONTRIBUTING.md)

## 🤝 Contributing

We welcome all forms of contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) to get involved.

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Thanks to all developers who have contributed to AIGEO!

---

**AIGEO** - White-hat GEO Content Credibility Assessment Framework  
Let quality content be understood and trusted by AI
```

### 3. LICENSE（MIT 推荐）

```
MIT License

Copyright (c) 2026 [Your Name or Organization]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 4. CONTRIBUTING.md

```markdown
# 贡献指南

感谢您对 AIGEO 的兴趣！我们欢迎所有形式的贡献。

## 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请：

1. 检查是否已有相关 issue
2. 如果没有，创建新的 issue，并包含：
   - 问题描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 环境信息（操作系统、Python版本等）

### 提交代码

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码风格
- 添加适当的注释和文档字符串
- 确保所有测试通过
- 更新相关文档

### 提交信息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

示例：
```
feat: add AI generation detection module

- Implement perplexity analysis
- Add burstiness calculation
- Include unit tests
```

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/aigeo.git
cd aigeo

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest
```

## 行为准则

请遵守我们的 [行为准则](CODE_OF_CONDUCT.md)。

## 问题？

如有任何问题，欢迎通过以下方式联系我们：
- 创建 Issue
- 发送邮件至：[your-email@example.com]

感谢您的贡献！
```

### 5. CODE_OF_CONDUCT.md

```markdown
# 行为准则

## 我们的承诺

为了营造一个开放和友好的环境，我们作为贡献者和维护者承诺：

- 尊重所有参与者，无论其经验水平、性别、性别认同和表达、性取向、残疾、个人外貌、体型、种族、民族、年龄、宗教或国籍
- 使用欢迎和包容的语言
- 接受建设性的批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

## 不可接受的行为

- 使用性化语言或图像，以及不受欢迎的性关注或 advances
- 挑衅、侮辱/贬损性评论，以及个人或政治攻击
- 公开或私下的骚扰
- 未经明确许可，发布他人的私人信息
- 其他在专业环境中被合理认为不适当的行为

## 我们的责任

项目维护者有责任澄清可接受行为的标准，并对任何不可接受行为采取适当和公平的纠正措施。

## 适用范围

本行为准则适用于所有项目空间，也适用于个人在公共空间代表项目或其社区时。

## 执行

可以通过 [your-email@example.com] 联系项目团队报告滥用、骚扰或其他不可接受的行为。

## 归属

本行为准则改编自 [Contributor Covenant](https://www.contributor-covenant.org/)，版本 2.0。
```

### 6. CHANGELOG.md

```markdown
# 更新日志

所有 notable 更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added
- 初始版本开发中

## [1.0.0] - 2026-03-08

### Added
- 初始发布 AIGEO 框架
- AI生成检测模块（困惑度、突发性分析）
- 事实核查模块（权威数据库匹配）
- 人类参与度评估（个人视角、独特经验）
- 可信度综合评分（0-100分）
- AI友好度增强（Schema.org标记生成）
- 完整的文档和示例

### Features
- 支持多种内容类型评估
- 提供详细的优化建议
- 可扩展的评估标准
- 开源评估框架

[Unreleased]: https://github.com/YOUR_USERNAME/aigeo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/YOUR_USERNAME/aigeo/releases/tag/v1.0.0
```

---

## 🎨 项目结构建议

```
aigeo/
├── .github/                    # GitHub 配置
│   ├── ISSUE_TEMPLATE/         # Issue 模板
│   ├── workflows/              # GitHub Actions
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                       # 文档
│   ├── quickstart.md
│   ├── api.md
│   └── criteria.md
├── src/                        # 源代码
│   └── aigeo/
│       ├── __init__.py
│       ├── assessor.py
│       ├── ai_detection.py
│       ├── fact_check.py
│       └── utils.py
├── tests/                      # 测试
│   └── test_assessor.py
├── examples/                   # 示例
│   └── basic_usage.py
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README_EN.md
├── requirements.txt
├── requirements-dev.txt
└── setup.py
```

---

## 🔧 高级配置

### GitHub Actions CI/CD

创建 `.github/workflows/ci.yml`：

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run tests
      run: pytest
    
    - name: Check code style
      run: flake8 src/
```

### Issue 模板

创建 `.github/ISSUE_TEMPLATE/bug_report.md`：

```markdown
---
name: Bug 报告
about: 创建报告以帮助我们改进
title: '[BUG] '
labels: bug
assignees: ''

---

**描述 Bug**
清晰简洁地描述 bug 是什么。

**复现步骤**
复现该行为的步骤：
1. 导入 '...'
2. 调用函数 '....'
3. 看到错误

**期望行为**
清晰简洁地描述您期望发生的情况。

**截图**
如果适用，添加截图以帮助解释您的问题。

**环境信息：**
 - 操作系统: [例如 iOS]
 - Python 版本: [例如 3.9]
 - AIGEO 版本: [例如 1.0.0]

**附加信息**
在此添加有关该问题的任何其他上下文。
```

---

## 📣 发布后推广

### 1. 社交媒体
- 在 Twitter、LinkedIn、知乎等平台分享
- 使用标签：#AIGEO #GEO #AI #开源

### 2. 技术社区
- 在 V2EX、掘金、CSDN 发布介绍文章
- 在 Reddit r/MachineLearning、r/opensource 分享

### 3. 相关项目
- 在 Awesome-GEO、Awesome-AI 等列表中添加
- 联系相关项目维护者合作

### 4. 邮件列表
- 发送邮件给潜在用户和贡献者
- 在相关邮件列表中分享

---

## ⚠️ 注意事项

1. **不要提交敏感信息**
   - API 密钥
   - 密码
   - 个人身份信息

2. **保持代码质量**
   - 编写测试
   - 添加文档
   - 遵循代码规范

3. **及时响应**
   - 回复 Issue 和 PR
   - 感谢贡献者
   - 保持项目活跃

4. **版本管理**
   - 使用语义化版本
   - 维护 CHANGELOG
   - 打标签发布

---

## 📞 获取帮助

如有问题，可以：
- 查看 [GitHub Docs](https://docs.github.com/)
- 搜索 [Stack Overflow](https://stackoverflow.com/)
- 联系 GitHub 支持

---

**祝您开源之旅顺利！** 🚀
