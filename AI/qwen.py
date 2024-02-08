from http import HTTPStatus
import dashscope


def chat_text_only(qwen_history, config, qwen_settings):
    dashscope.api_key = config['qwen']['api_key']
    response = dashscope.Generation.call(
        model=config['qwen']['model'],
        messages=qwen_history,
        seed=qwen_settings['seed'],
        max_tokens=qwen_settings['max_tokens'],
        top_p=qwen_settings['top_p'],
        top_k=qwen_settings['top_k'],
        repetition_penalty=qwen_settings['repetition_penalty'],
        temperature=qwen_settings['temperature'],
        stop=qwen_settings['stop'],
        stream=qwen_settings['stream'],
        enable_search=qwen_settings['enable_search'],
        result_format=qwen_settings['result_format'],
        incremental_output=qwen_settings['incremental_output'],
    )
    if response.status_code == HTTPStatus.OK:
        return response
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return response
