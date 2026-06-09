'''
让模型先“选择要不要调用函数 + 传什么参数”，再由你执行函数，最后把结果喂回模型。
'''

'''
用户提问
   ↓
LLM 判断是否需要工具
   ↓
返回“函数调用请求”（JSON）
   ↓
你的程序执行 Python 函数
   ↓
把结果再发给 LLM
   ↓
LLM生成最终回答
'''

# 假设有一个函数
def get_weather(city: str):
    return f"{city} 今天 28°C，晴天"

# 把函数描述给模型（非常关键）
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取城市天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# 让模型决定是否调用函数
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",  # 你的 Qwen（Ollama/vLLM）
    api_key="none"
)

response = client.chat.completions.create(
    model="qwen",
    messages=[
        {"role": "user", "content": "深圳今天天气怎么样？"}
    ],
    tools=tools,
    tool_choice="auto"
)

# 拿到函数调用请求
{
  "choices": [
    {
      "message": {
        "tool_calls": [
          {
            "function": {
              "name": "get_weather",
              "arguments": "{\"city\":\"深圳\"}"
            }
          }
        ]
      }
    }
  ]
}

# 执行函数
import json
tool_call = response.choices[0].message.tool_calls[0]
func_name = tool_call.function.name
args = json.loads(tool_call.function.arguments)
if func_name == "get_weather":
    result = get_weather(**args)

# 把结果交给模型
messages = [
    {"role": "user", "content": "深圳今天天气怎么样？"},
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    }
]
final_response = client.chat.completions.create(
    model="qwen",
    messages=messages
)
print(final_response.choices[0].message.content)