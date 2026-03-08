# AIGEO 架构设计

> 模块化、可扩展的白帽GEO内容可信度评估框架

---

## 架构概览

```
┌─────────────────────────────────────────────────────────────────┐
│                        AIGEO Framework                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   采集层     │  │   评估层     │  │   增强层     │          │
│  │  Collection  │  │  Assessment  │  │ Enhancement  │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                  │
│         └─────────────────┼─────────────────┘                  │
│                           │                                    │
│                    ┌──────┴──────┐                            │
│                    │   核心引擎   │                            │
│                    │ Core Engine │                            │
│                    └──────┬──────┘                            │
│                           │                                    │
│         ┌─────────────────┼─────────────────┐                  │
│         │                 │                 │                  │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐          │
│  │  信源网络   │  │  知识图谱   │  │  数据存储   │          │
│  │   Source   │  │ Knowledge  │  │  Storage   │          │
│  │  Network   │  │   Graph    │  │            │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 核心模块

### 1. 采集层 (Collection Layer)

负责从各种来源采集内容数据。

#### 1.1 AI平台适配器 (AI Platform Adapters)

**设计原则**: 可插拔架构，支持多种AI平台

```python
# 抽象基类
class AIPlatformAdapter(ABC):
    @abstractmethod
    def fetch_mentions(self, brand: str) -> List[Mention]:
        """获取品牌在AI回答中的提及"""
        pass
    
    @abstractmethod
    def query(self, question: str) -> Answer:
        """向AI平台提问"""
        pass

# 具体实现
class ChatGPTAdapter(AIPlatformAdapter):
    """OpenAI ChatGPT适配器"""
    pass

class DeepSeekAdapter(AIPlatformAdapter):
    """DeepSeek适配器"""
    pass

class ClaudeAdapter(AIPlatformAdapter):
    """Anthropic Claude适配器"""
    pass

class PerplexityAdapter(AIPlatformAdapter):
    """Perplexity适配器"""
    pass
```

**支持的AI平台**:
| 平台 | 状态 | 优先级 |
|------|------|--------|
| ChatGPT | ✅ 已实现 | P0 |
| DeepSeek | ✅ 已实现 | P0 |
| Claude | 🔄 计划中 | P1 |
| Perplexity | 🔄 计划中 | P1 |
| Gemini | 📋 待开发 | P2 |
| 文心一言 | 📋 待开发 | P2 |

#### 1.2 网页爬虫 (Web Crawler)

- 采集公开网页内容
- 遵守 robots.txt
- 支持分布式爬取
- 智能反爬策略

#### 1.3 API集成 (API Integration)

- 官方API接入
- 第三方数据服务
- 实时数据流

---

### 2. 评估层 (Assessment Layer)

核心评估引擎，对内容进行多维度可信度评估。

#### 2.1 AI生成检测模块 (AI Generation Detection)

**功能**: 识别内容是否由AI生成

**算法**:
```python
class AIGenerationDetector:
    def detect(self, text: str) -> DetectionResult:
        # 1. 困惑度分析 (Perplexity)
        perplexity = self.calculate_perplexity(text)
        
        # 2. 突发性分析 (Burstiness)
        burstiness = self.calculate_burstiness(text)
        
        # 3. 重复度分析 (Repetition)
        repetition = self.calculate_repetition(text)
        
        # 4. 综合评分
        score = self.ensemble_score(perplexity, burstiness, repetition)
        
        return DetectionResult(
            is_ai_generated=score > threshold,
            confidence=score,
            features={
                'perplexity': perplexity,
                'burstiness': burstiness,
                'repetition': repetition
            }
        )
```

**模型**:
- 基础模型: RoBERTa / DeBERTa
- 微调数据: 人工标注的AI/人类文本对
- 准确率目标: >90%

#### 2.2 原创性检测模块 (Originality Detection)

**功能**: 检测内容原创性，避免抄袭

**方法**:
- 文本相似度比对
- 语义相似度分析
- 引用溯源

**比对源**:
- 权威百科 (Wikipedia, 百度百科)
- 行业报告
- 主流媒体
- 学术论文

#### 2.3 事实核查模块 (Fact Verification)

**功能**: 验证内容中的事实声明

**流程**:
```
文本输入
    ↓
实体识别 (NER)
    ↓
关系抽取
    ↓
事实声明提取
    ↓
权威数据库匹配
    ↓
结果输出:
  - ✅ 已验证
  - ⚠️ 部分验证
  - ❌ 无法验证 / 冲突
```

**权威数据库**:
| 类型 | 来源 | 覆盖领域 |
|------|------|----------|
| 政府数据 | 统计局、各部委 | 经济、人口、政策 |
| 学术数据 | Google Scholar, CNKI | 学术研究 |
| 行业数据 | IDC, Gartner, 艾瑞 | 行业报告 |
| 百科数据 | Wikipedia, 百度百科 | 通用知识 |

#### 2.4 人类参与度评估模块 (Human Contribution Assessment)

**功能**: 评估内容中人类创作的成分

**评估维度**:
- 个人视角 (Personal Perspective)
- 独特经验 (Unique Experience)
- 情感表达 (Emotional Expression)
- 创造性见解 (Creative Insight)

**评分标准**:
```python
class HumanContributionScorer:
    def score(self, text: str) -> Score:
        return Score(
            personal_perspective=self.detect_personal_perspective(text),
            unique_experience=self.detect_unique_experience(text),
            emotional_expression=self.detect_emotional_expression(text),
            creative_insight=self.detect_creative_insight(text)
        )
```

#### 2.5 可信度综合评分 (Credibility Scoring)

**综合算法**:
```python
class CredibilityScorer:
    def calculate(self, content: Content) -> CredibilityScore:
        # 各维度评分
        ai_score = self.ai_detector.detect(content.text)
        originality_score = self.originality_checker.check(content.text)
        fact_score = self.fact_verifier.verify(content.text)
        human_score = self.human_scorer.score(content.text)
        
        # 加权综合
        final_score = (
            ai_score * 0.25 +
            originality_score * 0.20 +
            fact_score * 0.30 +
            human_score * 0.25
        )
        
        return CredibilityScore(
            total=final_score,
            breakdown={
                'ai_generation': ai_score,
                'originality': originality_score,
                'fact_verification': fact_score,
                'human_contribution': human_score
            },
            suggestions=self.generate_suggestions(final_score, breakdown)
        )
```

**评分等级**:
| 分数 | 等级 | 说明 |
|------|------|------|
| 90-100 | 🟢 优秀 | 高度可信，推荐引用 |
| 70-89 | 🟡 良好 | 基本可信，建议优化 |
| 50-69 | 🟠 一般 | 可信度存疑，需改进 |
| 0-49 | 🔴 低质 | 不可信，不建议引用 |

---

### 3. 增强层 (Enhancement Layer)

帮助内容创作者优化内容，提升AI友好度。

#### 3.1 结构化标记生成器 (Structured Markup Generator)

**功能**: 自动生成Schema.org标记

**支持的Schema类型**:
- Article (文章)
- NewsArticle (新闻)
- BlogPosting (博客)
- Product (产品)
- FAQPage (FAQ)
- Person (人物)
- Organization (组织)
- Event (事件)

**输出格式**: JSON-LD

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "文章标题",
  "author": {
    "@type": "Person",
    "name": "作者名"
  },
  "datePublished": "2026-03-08",
  "publisher": {
    "@type": "Organization",
    "name": "发布机构"
  }
}
```

#### 3.2 关键信息抽取器 (Key Information Extractor)

**功能**: 提取5W1H信息

```python
class InformationExtractor:
    def extract(self, text: str) -> StructuredInfo:
        return StructuredInfo(
            who=self.extract_who(text),
            when=self.extract_when(text),
            where=self.extract_where(text),
            what=self.extract_what(text),
            why=self.extract_why(text),
            how=self.extract_how(text)
        )
```

#### 3.3 AI友好度评分器 (AI-Friendly Scorer)

**评估维度**:
- 标题清晰度
- 段落结构
- 信息密度
- 标记完整性
- 语义连贯性

**优化建议**:
- 标题优化建议
- 结构调整建议
- 标记补充建议

#### 3.4 一键优化器 (One-Click Optimizer)

**功能**: 自动生成优化后的内容

**流程**:
```
原始内容
    ↓
可信度评估
    ↓
问题识别
    ↓
优化建议生成
    ↓
用户确认
    ↓
生成优化版本
    ↓
输出HTML/JSON-LD
```

---

### 4. 信源网络 (Source Network)

#### 4.1 权威信源库 (Authoritative Source Database)

**信源评分算法**:
```python
class SourceScorer:
    def calculate(self, source: Source) -> SourceScore:
        # 基础分 (域名类型)
        base_score = self.domain_type_score(source.domain)
        
        # 声誉分 (第三方权威度)
        reputation_score = self.reputation_assessment(source)
        
        # 影响力分 (被引用次数/质量)
        influence_score = self.citation_analysis(source)
        
        # 真实性分 (作者/联系方式/数据来源)
        authenticity_score = self.authenticity_check(source)
        
        # 动态调整
        time_factor = self.time_decay(source.last_updated)
        
        return SourceScore(
            total=(base_score + reputation_score + 
                   influence_score + authenticity_score) * time_factor,
            components={
                'base': base_score,
                'reputation': reputation_score,
                'influence': influence_score,
                'authenticity': authenticity_score
            }
        )
```

**观察期机制**:
- 新发现信源需经过30天观察期
- 积累足够引用数据后方可进入高分库

#### 4.2 污染源黑名单 (Pollution Source Blacklist)

**识别标准**:
- 批量生成低质内容
- 虚假信息传播
- 恶意SEO操纵
- 无作者/联系方式

**社区参与**:
- 用户举报机制
- 专家审核
- 定期更新

#### 4.3 引用关系图谱 (Citation Graph)

**功能**: 可视化内容引用关系

```
用户内容
    ├── 引用: 权威来源A (权重: 0.9)
    ├── 引用: 权威来源B (权重: 0.8)
    └── 引用: 一般来源C (权重: 0.5)
        
被引用分析:
    ├── 被: 权威网站X引用
    └── 被: 博客Y引用
```

---

### 5. 知识图谱 (Knowledge Graph)

#### 5.1 实体关系图谱

**实体类型**:
- 品牌 (Brand)
- 产品 (Product)
- 人物 (Person)
- 组织 (Organization)
- 事件 (Event)
- 概念 (Concept)

**关系类型**:
- 竞争关系 (competes_with)
- 合作关系 (partners_with)
- 包含关系 (contains)
- 引用关系 (cites)
- 归属关系 (belongs_to)

#### 5.2 行业知识图谱

**覆盖行业**:
- 科技/互联网
- 金融/投资
- 医疗健康
- 教育培训
- 电商零售
- 制造业

---

### 6. 数据存储 (Storage)

#### 6.1 向量数据库 (Vector DB)

**用途**: 存储内容嵌入向量，用于相似度检索

**选型**: Pinecone / Milvus / Weaviate

#### 6.2 关系数据库 (Relational DB)

**用途**: 用户信息、任务记录、评估结果

**选型**: PostgreSQL / MySQL

#### 6.3 对象存储 (Object Storage)

**用途**: 原始爬取内容、报告文件

**选型**: AWS S3 / MinIO / 阿里云OSS

---

## 扩展性设计

### 插件系统 (Plugin System)

```python
class PluginInterface(ABC):
    @abstractmethod
    def initialize(self, config: dict):
        pass
    
    @abstractmethod
    def execute(self, data: Any) -> Any:
        pass

# 示例: 自定义评估插件
class CustomAssessmentPlugin(PluginInterface):
    def initialize(self, config: dict):
        self.model = load_model(config['model_path'])
    
    def execute(self, content: Content) -> AssessmentResult:
        return self.model.assess(content)
```

### API接口 (API Interface)

**RESTful API**:
```
POST /api/v1/assess
  - 评估内容可信度

GET /api/v1/sources
  - 获取信源列表

POST /api/v1/enhance
  - 优化内容

GET /api/v1/metrics
  - 获取评估指标
```

**GraphQL API** (可选):
```graphql
type Query {
  assessContent(text: String!): CredibilityScore
  getSource(id: ID!): Source
  listSources(filter: SourceFilter): [Source]
}
```

---

## 部署架构

### 单机部署

```
[用户] → [AIGEO Core] → [本地数据库]
              ↓
         [本地文件存储]
```

### 分布式部署

```
[负载均衡] → [API Gateway]
                ↓
    ┌──────────┼──────────┐
    ↓          ↓          ↓
[评估服务]  [采集服务]  [增强服务]
    ↓          ↓          ↓
[Redis缓存] [消息队列] [任务调度]
    ↓          ↓          ↓
[PostgreSQL] [Vector DB] [对象存储]
```

---

## 技术栈

| 层级 | 技术选型 |
|------|----------|
| **编程语言** | Python 3.8+ |
| **Web框架** | FastAPI / Flask |
| **机器学习** | PyTorch, Transformers |
| **NLP** | spaCy, NLTK, Jieba |
| **数据库** | PostgreSQL, Redis, Milvus |
| **消息队列** | Celery + RabbitMQ / Redis |
| **容器化** | Docker, Kubernetes |
| **监控** | Prometheus, Grafana |

---

## 开发路线图

### Phase 1: 核心框架 (已完成 ✅)
- [x] 基础架构设计
- [x] AI生成检测
- [x] 事实核查基础功能
- [x] 可信度评分

### Phase 2: 功能完善 (进行中 🔄)
- [ ] 更多AI平台适配器
- [ ] 权威信源库扩展
- [ ] 知识图谱构建
- [ ] API接口完善

### Phase 3: 生态建设 (计划中 📋)
- [ ] 插件系统
- [ ] 社区贡献平台
- [ ] 行业标准制定
- [ ] 商业化支持

---

## 贡献指南

### 如何贡献模块

1. **Fork 仓库**
2. **创建特性分支** (`git checkout -b feature/new-adapter`)
3. **实现模块** (遵循接口规范)
4. **添加测试** (单元测试 + 集成测试)
5. **更新文档** (API文档 + 使用示例)
6. **提交 PR** (描述清楚改动内容)

### 模块开发规范

- 遵循 PEP 8 代码风格
- 添加类型注解
- 编写 docstring
- 单元测试覆盖率 >80%
- 提供使用示例

---

**AIGEO 架构设计**  
*模块化、可扩展、白帽优先*
