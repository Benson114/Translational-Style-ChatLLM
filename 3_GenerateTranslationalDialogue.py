# %%
import time
import jsonlines
from src import MyOpenAI, Prompts
from concurrent.futures import ThreadPoolExecutor, as_completed

kwargs = {
    "max_tokens": 2048,
    "temperature": 2.0,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 1.0,
    "stop": [],
}
n_workers = 8


# %%
def generate_translational_dialogue(dialogue):
    global response
    dialogue.pop("topic", None)
    user_input = Prompts.prompt3(dialogue)
    messages = [{"role": "system", "content": user_input}]
    try:
        response = MyOpenAI.chat(messages, kwargs)
        dialogue = MyOpenAI.parse(response)
        dialogue = eval(dialogue)
        if isinstance(dialogue, dict) and "问" in dialogue and "答" in dialogue:
            return dialogue
    except Exception as e:
        return f"Error: {e}", response


# %%
translational_dialogues = []
errors = []
with jsonlines.open("GPTGenerateData/2_Dialogues.jsonl") as reader:
    dialogues = [dialogue for dialogue in reader]

with ThreadPoolExecutor(max_workers=n_workers) as executor:
    futures = [executor.submit(generate_translational_dialogue, dialogue) for dialogue in dialogues]
    start = time.time()
    for future in as_completed(futures):
        res = future.result()
        if isinstance(res, dict):
            translational_dialogues.append(res)
            end = time.time()
            print(
                f"Generated {len(translational_dialogues)} translational dialogues. "
                f"Time elapsed: {end - start:.2f}s"
            )
        else:
            e, response = res
            errors.append(response)
            print(e)

# %%
with jsonlines.open("GPTGenerateData/3_TranslationalDialogues.jsonl", "w") as writer:
    for res in translational_dialogues:
        writer.write(res)

# %%
with jsonlines.open("GPTGenerateData/Errors_TranslationalDialogues.jsonl", "w") as writer:
    for res in errors:
        writer.write(str(res))
