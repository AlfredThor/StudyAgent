#### RAG

**概念**

> RAG是Retrieval-Augmented Generation（检索增强生成）的缩写，是目前大语言模型（LLM）最常用的知识增强技术之一。简单说：先查资料，再让AI
> 根据查询的资料生成答案。

**为什么需要RAG？**

目前大模型有两个问题：

1、知识过时
  - 模型训练完成后，无法自动知道新发生的事情。
  - 例如新发布的产品、最新的政策等。

2、容易幻觉（Hallucination）
  - 模型可能一本正经的编造答案。
  - 尤其是企业内部知识、专业文档等训练时没见过的信息

---

#### Agent

**核心能力：**

> 让大模型能够自主规划、调用工具、执行步骤，并根据结果继续行动，直到完成目标。

#### Agent学习过程

**第一阶段（简单Agent 1-2周）：**

目标：

- 调用LLM API
- 实现Function Calling（模型函数调用）
- 接入工具
- 多伦对话记忆

学习内容：

- Prompt Engineering（提示词工程）
- Tool Calling（工具调用）
- Structured Output
- OpenAI SDK
- MCP（Model Context Protocol）

**第二阶段（能做业务Agent 2-4周）：**

目标：

- 多工具调用
- 工作流安排
- Agent状态管理
- 长短期记忆

学习：

- LangGraph
- PydanticAI
- Agno
- MCP Server

**第三阶段（多Agent系统 1-2个月）：**

目标：

- 多个Agent协同工作

涉及：

- Agent Router
- Agent Team
- Agent Memory
- Agent Planning
- Agent Reflection

---

#### 项目实战（第一天）

> 将博客系统、模型 封装进Fastapi服务中