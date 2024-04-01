from openai import OpenAI

api_key = ""  # Your API key
base_url = None  # The base URL for the API, if any
model = "gpt-3.5-turbo"  # Model name

client = OpenAI(api_key=api_key, base_url=base_url)


def chat(messages, kwargs):
    response = client.chat.completions.create(messages=messages, model=model, **kwargs)
    return response


def parse(response):
    return response.choices[0].message.content
