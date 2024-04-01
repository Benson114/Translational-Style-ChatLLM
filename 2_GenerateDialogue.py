# %%
import time
import jsonlines
import itertools
from src import MyOpenAI, Prompts
from concurrent.futures import ThreadPoolExecutor, as_completed

kwargs = {
    "max_tokens": 2048,
    "temperature": 1.2,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 1.0,
    "stop": [],
}
n_dataset = 32
n_workers = 8

# %%
topics = []
with open("GPTGenerateData/1_Topics.txt", "r", encoding="utf-8") as f:
    topics = [line.strip() for line in f]

topic_iterator = itertools.cycle(topics)


# %%
def generate_dialogue(topic):
    user_input = Prompts.prompt2(topic)
    messages = [{"role": "system", "content": user_input}]
    try:
        response = MyOpenAI.chat(messages, kwargs)
        dialogue = MyOpenAI.parse(response)
        dialogue = eval(dialogue)
        if isinstance(dialogue, dict) and "问" in dialogue and "答" in dialogue:
            dialogue["topic"] = topic
            return dialogue
    except Exception as e:
        return f"Error: {e}"


# %%
dialogues = []
with ThreadPoolExecutor(max_workers=n_workers) as executor:
    futures = [executor.submit(generate_dialogue, topic) for topic in
               itertools.islice(topic_iterator, n_workers * n_dataset)]
    start = time.time()
    for future in as_completed(futures):
        dialogue = future.result()
        if isinstance(dialogue, dict):
            dialogues.append(dialogue)
            end = time.time()
            print(
                f"Generated {len(dialogues)} dialogues. "
                f"Time elapsed: {end - start:.2f}s"
            )
        else:
            print(dialogue)

        if len(dialogues) >= n_dataset:
            print("Reached the target number of dialogues.")
            executor.shutdown(wait=False)
            break

# %%
with jsonlines.open("GPTGenerateData/2_Dialogues.jsonl", "a") as f:
    f.write_all(dialogues)

# %%
