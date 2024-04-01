# %%
import json

dataset = []
with open("GPTGenerateData/3_TranslationalDialogues.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        new_data = {
            "instruction": "",
            "input": data["问"],
            "output": data["答"],
        }
        dataset.append(new_data)

with open("GPTGenerateData/TslDial.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

# %%
