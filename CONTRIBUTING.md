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
git clone https://github.com/q86830-hue/aigeo.git
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
- 发送邮件至：spring60@vip.qq.com

感谢您的贡献！
