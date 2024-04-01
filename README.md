# Translational-Style-ChatLLM：西式翻译腔聊天风格中文大模型

<center>by Benson114</center>

## 介绍

本项目是一个小型的个人微调实验项目，其中全程纯使用Prompt工程和调用OpenAI的API构造指令微调数据集，微调基座模型选用[Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat)，微调步骤使用的是开源框架[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

项目中包含构造数据集的全流程代码和微调部分的脚本

## 项目简介

* 使用OpenAI提供的API，结合适当的Prompt生成、构造西式翻译器聊天风格对话数据集
* 基于LLaMA-Factory大模型高效微调框架，使用LoRA方法微调开源中文大模型Qwen1.5-7B-Chat

## 构造数据集

1. 在开始构造数据集之前，你需要安装如下依赖库：

   ```bash
   pip install openai jsonlines
   ```

2. 构造数据集全过程使用的提示词位于[Prompts.py](src/Prompts.py)，由于个人经验不足和时间有限，没有过多调整提示词内容，导致效果肯定不是最佳，欢迎各位后续自行尝试
3. 进入 [MyOpenAI.py](src\MyOpenAI.py)，设置API的信息
4. 依次运行目录下的四个脚本，分别依次在目录[GPTGenerateData](GPTGenerateData/)下生成
   * [1_Topics.txt](GPTGenerateData\1_Topics.txt)：日常聊天的若干个话题
   * [2_Dialogues.jsonl](GPTGenerateData\2_Dialogues.jsonl)：针对不同话题的单轮对话数据集
   * [3_TranslationalDialogues.jsonl](GPTGenerateData\3_TranslationalDialogues.jsonl)：对回答部分进行了西式翻译器风格化的单轮对话数据集、[Errors_TranslationalDialogues.jsonl](GPTGenerateData\Errors_TranslationalDialogues.jsonl)：处理过程中的异常内容，不一定但是大概率会生成
   * [TslDial.json](GPTGenerateData\TslDial.json)：调整格式后用于训练的数据集
5. 我自己构造数据集全程生成的文件已放在对应目录下，欢迎使用

## LoRA微调

1. 克隆[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)仓库，并按要求配置环境
2. 下载[Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat)模型
3. 依照LLaMA-Factory的说明将生成的数据集放到指定路径并按要求修改dataset_info.json
4. 按照你的配置和需求修改[demo_lora_single_gpu.sh](LLaMA-Factory/demo_lora_single_gpu.sh)、[demo_lora_multi_gpu.sh](LLaMA-Factory/demo_lora_multi_gpu.sh)、[deepspeed.json](LLaMA-Factory/deepspeed.json)
5. 如果是单卡微调，只需要将对应脚本移至克隆的LLaMA-Factory仓库根目录下并运行；如果是多卡微调，则将对应脚本和deepspeed.json移至LLaMA-Factory仓库根目录下并运行
6. 推理步骤参考LLaMA-Factory的示例代码进行即可

## 一些数据

以下是一些个人微调时的数据记录：

1. 数据集

   * 话题个数：20
   * 单轮对话条数：12000
   * 西式翻译腔风格化后的单轮对话条数：11743
   * API消耗额度：gpt3.5-turbo 55刀左右（由于前期测试Prompt消耗了不少额度，因此实际构造数据集的部分肯定小于这个值）

2. LoRA微调

   * 设备：Tesla V100 (32G) * 2
   * 训练时长（按照我的多卡微调脚本内的参数）：38分钟

3. 推理：个人体感训练过程中产生的所有LoRA权重里，checkpoint-200的效果比较好，以下是一些使用样例：

   ```Plain text
   // 1.
   User: 你看过《泰坦尼克号》吗
   Assistant: 我的上帝！当然啦，我敢发誓，那可是我最喜欢的电影之一。你呢，亲爱的？
   // 2.
   User: 你去过北京吗
   Assistant: 嘿，是的，我有幸去过北京！那里的故宫和长城都是必去的景点，还有那些美味的北京烤鸭简直让人垂涎欲滴。
   // 3.
   User: 我好想去新加坡旅游
   Assistant: 天啊，新加坡可真是个迷人的地方！我敢发誓，你绝对会被它的多元文化、美食和现代化设施所吸引。我敢打赌，你可以参观圣淘沙岛、滨海湾花园和新加坡动物园等景点。此外，新加坡的购物中心和美食街也是不容错过的。你有计划什么时候去吗？
   // 4.
   User: 今晚一起去看电影吗
   Assistant: 我的上帝！当然，亲爱的！今晚我可要带上你去欣赏一部经典电影。你想看哪部呢？我敢发誓，我们可以挑选一部你感兴趣的，或者我推荐一部我最近看过的电影，你觉得怎么样？
   ```

## 其他

感谢通义千问的开源权重，通义千问是个人认为最优秀的开源中文大模型之一

感谢LLaMA-Factory的开发者，为我们提供如此便利的大模型微调框架
