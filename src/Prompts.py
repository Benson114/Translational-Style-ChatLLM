def prompt1():
    return ("列出20个日常聊天的主题，例如美食、旅游。"
            "\n返回的内容遵循Python的列表格式，如：['美食', '旅游', ...]")


def prompt2(topic):
    return (f"生成一轮聊天对话，主题为{topic}。对话形式为一人发起聊天话题，另一人作出回应。"
            f"\n返回的内容遵循Python的字典格式，如：{'{'}'问': （xxx）, '答': （xxx）{'}'}")


def prompt3(dialogue):
    return (f"将一段中文对话文本的回答部分重构为具有西方翻译腔特色的回答。"
            f"\n西方翻译腔特色包括："
            f"\n1.使用感叹词如“噢”、“嘿”、“天啊”、“是的”；"
            f"\n2.加入“我的上帝！”、“耶和华啊！”、“可敬的圣母玛利亚！”、“耶稣保佑”、“我敢发誓”等短语；"
            f"\n3.讲话要客气，即使是批评也要用“该死”、“讨厌”、“混蛋”甚至是“我可要狠狠地踢你的屁股了”等词；"
            f"\n4.使用亲昵的称呼如“宝贝儿”，“我的甜心”，“亲爱的xxx”，“迷人的xxx”，“老伙计”，“我的朋友”，“xxx先生”，“xxx女士”。"
            f"\n仅重构回答部分，务必保持问题部分不变。"
            f"\n以下是一段具有强烈西方翻译腔特色的对话，供参考："
            f"\nT：噢，亲爱的弗雷泽小姐，见到你真是太开心了。说真的，你看起来不错，肯定是这样的，难道不是么？"
            f"\nF：嘿，迷人的汤普森小姐，你看起来也不错，我是说，容光焕发的那种，我敢打赌，你肯定有什么好事要告诉我。"
            f"\nT：哦，我亲爱的弗雷泽小姐，瞧我这个记性，简直和隔壁宿舍塔娄太太养的那两只蠢乌龟一样差了，"
            f"鬼知道我最近这是怎么了。噢，抱歉，我是说，我差点忘了告诉你一个特别重要的事情。"
            f"\nF：哈，瞧你说的，我亲爱的汤普森小姐。嘿，你到底要跟我说什么呀？你总是喜欢这么吊人胃口。"
            f"\nT：噢，我亲爱的弗雷泽小姐，你听完后可别惊掉了下巴，我们要发财了——大学生创业，你肯定听说过。"
            f"我是说，我们可以在宿舍卖煎鸡蛋——就用这个，喏，煎蛋器，我敢保证，我们肯定能狠狠地赚上一大笔美金，"
            f"你等着吧，到时候我们就可以给沙河校区也买一个马走日雕像了——我知道你一直想这么做，不是么？"
            f"\n我需要你重构的对话：{dialogue}"
            f"\n你的返回格式为：{'{'}'问': 原问题, '答': 重构后的回答{'}'}")
