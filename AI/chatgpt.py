from openai import OpenAI
def chat_text_only(chatgpt_history, config, chatgpt_settings):
    client = OpenAI(api_key=config['gpt']['api_key'])
    proxy_url = config['gpt']['proxy_url']
    if not proxy_url.endswith("/v1"):
        proxy_url = proxy_url + "/v1"
    client.base_url = proxy_url
    completion = client.chat.completions.create(
        model=chatgpt_settings['model'],
        messages=chatgpt_history,
        max_tokens=chatgpt_settings['max_tokens'],
        temperature=chatgpt_settings['temperature']
    )
    return completion