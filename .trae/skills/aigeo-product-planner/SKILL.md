---
name: "aigeo-product-planner"
description: "AIGEO白帽GEO品牌AI可见性管理平台的产品规划助手。Invoke when user needs to create product requirements, feature specifications, user stories, or technical architecture for GEO (Generative Engine Optimization) platforms. Helps with AI mention monitoring, content credibility assessment, and AI-friendly content optimization planning."
---

# AIGEO Product Planner

## Overview

AIGEO是一款**白帽GEO品牌AI可见性管理平台**，帮助品牌通过**真实、可信、结构化**的内容，在生成式AI答案中获得优先推荐，同时通过治理污染信源，维护健康的AI信息生态。

**核心价值**：让优质内容被AI理解并信任，让污染无处遁形。

## When to Invoke

Invoke this skill when:
- Creating product requirements for GEO/AI visibility platforms
- Designing features for AI mention monitoring and analysis
- Planning content credibility assessment systems
- Building AI-friendly content optimization tools
- Developing authoritative source network engines
- Creating technical architecture for GEO platforms

## Core Modules

### 1. 诊断与监测中心 (Diagnostics & Monitoring)

**Key Features:**
- **AI Mention Scanner**: Crawl major AI platforms (ChatGPT, DeepSeek, Claude, Perplexity) for brand mentions
- **Answer Share Analysis**: Track brand vs competitor mention frequency, ranking, sentiment
- **Sentiment Alert**: Real-time alerts for negative or incorrect AI answers
- **Historical Trends**: Track AI visibility changes over time

**User Stories:**
- Brand managers want to know brand mention status in AI answers
- Compare with competitors to adjust marketing strategy

### 2. 内容可信度评估引擎 (Content Credibility Engine)

**Key Features:**
- **AI Generation Detection**: Analyze perplexity, burstiness for AI traces
- **Originality Check**: Compare with authoritative sources (encyclopedias, reports, media)
- **Fact Verification**: Match claims with authoritative databases (gov stats, academic papers)
- **Human Contribution Score**: Evaluate personal perspective, unique experience, specific cases
- **Credibility Score**: Comprehensive 0-100 score with optimization suggestions

**Algorithms:**
- Fine-tuned RoBERTa/DeBERTa for AI detection
- Entity linking and relation extraction for fact checking
- BERT-based sentiment analysis

### 3. AI友好度增强引擎 (AI-Friendly Enhancement)

**Key Features:**
- **Structured Markup Generator**: Auto-generate Schema.org markup (JSON-LD)
- **Key Info Extraction**: Extract 5W1H in structured format
- **Controversy Annotation**: Suggest "according to XX research" for uncertain topics
- **AI-Friendly Score**: Evaluate title clarity, paragraph structure, info density
- **One-Click Optimization**: Generate optimized HTML code

**Technical Approach:**
- LLM (GPT-4/Claude) for information extraction
- Schema.org API integration

### 4. 信源网络构建引擎 (Source Network Builder)

**Key Features:**
- **Authoritative Source Database**: Dynamic database with domain reputation, influence, authenticity scores
- **Media Matching**: Recommend AI-cited platforms by industry/topic
- **Content Multiplication**: Break reports into articles, Q&A, infographics for different platforms
- **Citation Graph**: Visualize content citations and source authority
- **Fake Network Detection**: Warn against low-quality link farms

**Authority Scoring Algorithm:**
```
Score = Base (domain type) + Reputation + Influence (citations) + Authenticity
New sources require 30-day observation period before high-score entry
```

### 5. 效果追踪与策略优化 (Performance Tracking)

**Key Features:**
- **AI Ranking Monitor**: Regular queries to track brand position in AI answers
- **Competitor Intelligence**: Auto-compare competitor mentions, new sources
- **Strategy Recommendations**: AI-generated suggestions based on monitoring data
- **Weekly Reports**: Key metrics and actionable insights

## Technical Architecture

```
[Frontend] (Web/App)
    ↓
[API Gateway]
    ↓
[Microservices]
├── Data Collection (Crawler + AI Platform APIs)
├── NLP Analysis (Entity Recognition, Sentiment, Extraction)
├── Content Optimization (LLM + Schema Generation)
├── Source Database (Authority Index)
├── User/Billing Service
└── Scheduled Tasks (Periodic Monitoring)
    ↓
[Data Layer]
├── Vector DB (Content embeddings for similarity)
├── Relational DB (Users, tasks)
└── Object Storage (Raw content, reports)
    ↓
[AI Layer]
├── LLM APIs (GPT-4, Claude)
├── Fine-tuned Models (GEO-specific)
└── Knowledge Graph (Brand-Product-Competitor)
```

## Development Roadmap

### Phase 1: MVP (1-2 months)
- AI mention scanning (2-3 platforms: ChatGPT, DeepSeek)
- Basic sentiment alerts
- Dashboard with mention counts and trends
- User registration/login
- **Success**: 100 beta users, >1000 daily scans

### Phase 2: Core Features (3-4 months)
- Content credibility engine (AI detection, originality, scoring)
- AI-friendly enhancement (Schema markup, scoring)
- Authoritative source database V1.0
- Competitor analysis
- **Success**: >40% retention, >30% optimization completion

### Phase 3: Intelligence & Ecosystem (5-6 months)
- Source network builder (media matching, citation graph)
- Strategy recommendations (data + LLM)
- Mobile app
- API interface
- **Success**: >5% conversion, >100K API calls/month

### Phase 4: Optimization & Expansion (6+ months)
- More AI platforms (Claude, Perplexity, domestic models)
- Industry knowledge graphs
- GEO industry standards and whitepapers

## Key Algorithms

### Authority Source Scoring
- Base score (domain type: .gov/.edu)
- Reputation score (third-party authority)
- Influence score (citation count/quality)
- Authenticity score (author/contact/data source)
- Dynamic updates with 30-day observation period

### AI Generation Detection
- Fine-tuned RoBERTa/DeBERTa
- Features: perplexity, burstiness, repetition
- Output: AI generation probability

### Fact Verification
- Build fact database (gov stats, academic papers, industry reports)
- Entity linking and relation extraction
- Flag unmatched claims as "needs verification"

## Success Metrics (OKRs)

### Objective 1: Market Leadership in White-Hat GEO
- KR1: 1000 enterprise users in 6 months, >50 paid
- KR2: GEO industry whitepaper cited by 3+ authoritative media
- KR3: Data partnerships with 5 major AI platforms

### Objective 2: Industry-Leading Core Features
- KR1: >100K high-quality domains in authority database
- KR2: >85% fact-check accuracy, >90% AI detection accuracy
- KR3: 30% average increase in AI mention rate after optimization

### Objective 3: Healthy GEO Ecosystem
- KR1: Identify and flag >10K low-quality sources
- KR2: 50% increase in verified real data citations
- KR3: 2+ industry associations adopt GEO credibility standards

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| AI platform updates break crawling | High | High | Multi-strategy crawling; rapid adaptation |
| Data privacy/compliance issues | Medium | High | Public data only; clear user agreements; GDPR compliance |
| Black-hat competitor competition | Medium | Medium | White-hat education; industry standards; authority partnerships |
| User content quality varies | High | Medium | Credibility scoring guidance; reject low-quality content |
| Technical difficulty (fact checking) | High | Medium | Start with specific domains; crowdsourced verification |
| Business model sustainability | Medium | High | Tiered pricing; enterprise customization |

## Usage Guidelines

When helping with AIGEO product planning:

1. **Prioritize White-Hat Principles**: Emphasize real, credible, structured content over manipulation
2. **Focus on Measurable Value**: AI mention rates, credibility scores, sentiment trends
3. **Balance Automation and Human Review**: AI for scale, humans for quality judgment
4. **Build Trust Through Transparency**: Clear scoring methodologies, source attribution
5. **Plan for Ecosystem Health**: Include pollution detection and governance features

## Example User Requests

**User**: "Help me design the AI mention scanning feature"
**Response**: Focus on multi-platform coverage, real-time alerts, competitor benchmarking

**User**: "How should the credibility scoring work?"
**Response**: Multi-factor algorithm (AI detection, originality, fact verification, human contribution), transparent scoring, actionable improvements

**User**: "What's the technical architecture for GEO optimization?"
**Response**: Microservices for scalability, vector DB for similarity, LLM for content enhancement, knowledge graph for relationships
