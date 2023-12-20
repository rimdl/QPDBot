import AI.gemini as gemini


def chat(content, config, gemini_settings):
    if content['AI'] == 'gemini':
        if content['image'] == "":
            return gemini.chat_multi_turn(content['history'], config, gemini_settings)
    else:
        return "hgahah"
