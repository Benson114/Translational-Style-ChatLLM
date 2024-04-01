# %%
from src import MyOpenAI, Prompts

kwargs = {
    "max_tokens": 100,
    "temperature": 0.2,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 1.0,
    "stop": [],
}

# %%
user_input = Prompts.prompt1()
messages = [{"role": "user", "content": user_input}]

# %%
response = MyOpenAI.chat(messages, kwargs)
topics = MyOpenAI.parse(response)
topics = eval(topics)

# %%
print(topics)
with open("GPTGenerateData/1_Topics.txt", "w", encoding="utf-8") as f:
    for topic in topics:
        f.write(f"{topic}\n")

# %%
