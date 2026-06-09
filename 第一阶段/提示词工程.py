'''
一个标准的提示词通常由四部分组成：
角色（Role）
任务（Task）
约束（Constraints）
输出格式（Output Format）

Prompt Engineering在Agent中不是写文章工具，而是控制LLM行为逻辑的程序代码

Plain text
你是一个AI Agent，负责操作博客系统。

你可以使用以下工具：
- search_article
- get_article
- create_article

规则：
- 如果用户要查文章 -> 调用 search_article
- 如果用户要总结  -> 先获取文章再总结
- 必须优化使用工具

输出必须结构化
'''