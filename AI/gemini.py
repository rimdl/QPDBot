import base64
import io
import json
import requests
import PIL.Image
from io import BytesIO


def chat_text_only(text, config, gemini_settings):
    if text and config:
        proxy_url = config['gemini']['proxy_url']
        api_key = config['gemini']['api_key']
        model = config['gemini']['model']
        if not proxy_url.endswith("/"):
            proxy_url += "/"
        data = json.dumps({"contents": [{"parts": [{"text": text}]}],"safetySettings": gemini_settings['safetySettings'],"generationConfig": gemini_settings['generationConfig']})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(proxy_url + "v1beta/models/"+model+":generateContent?key=" + api_key, data=data,headers=headers)
        return response
    else:
        return None


def chat_text_and_image(image_url, text, config, gemini_settings):
    if image_url and text and config:
        proxy_url = config['gemini']['proxy_url']
        api_key = config['gemini']['api_key']
        if not proxy_url.endswith("/"):
            proxy_url += "/"
        img = PIL.Image.open(BytesIO(requests.get(image_url).content))
        img.resize((512, int(img.height * 512 / img.width)))
        img = img.convert('RGB')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode()
        data = json.dumps({"contents": [{"parts": [{"text": text}, {"inline_data": {"mime_type": "image/jpeg", "data": img_base64}}]}],"safetySettings": gemini_settings['safetySettings'],"generationConfig": gemini_settings['generationConfig']})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(proxy_url + "v1beta/models/gemini-pro-vision:generateContent?key=" + api_key,
                                 data=data, headers=headers)
        return response
    else:
        return None


def chat_multi_turn(history, config, gemini_settings):
    if history and config:
        history['safetySettings'] = gemini_settings['safetySettings']
        history['generationConfig'] = gemini_settings['generationConfig']
        proxy_url = config['gemini']['proxy_url']
        api_key = config['gemini']['api_key']
        model = config['gemini']['model']
        if not proxy_url.endswith("/"):
            proxy_url += "/"
        data = json.dumps(history)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(proxy_url + "v1beta/models/"+model+":generateContent?key=" + api_key, data=data,
                                 headers=headers)
        return response
