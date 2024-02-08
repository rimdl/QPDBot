import ast
import botpy
from botpy.message import Message
import AI.gemini as gemini
import AI.chatgpt as gpt
import AI.qwen as qwen
import utils.check_url as check_url
import utils.text2image as text2image


class MyClient(botpy.Client):
    sys_path = ""
    config = None
    gemini_settings = None
    chatgpt_settings = None
    qwen_settings = None
    help = None
    chatbot = gemini
    reply_text = ""
    gemini_history = {'contents': []}
    chatgpt_history = []
    qwen_history = []

    def __init__(self, intents,bot):
        super().__init__(intents)
        if bot == "gemini":
            self.chatbot = gemini
        elif bot == "gpt":
            self.chatbot = gpt
        elif bot == "qwen":
            self.chatbot = qwen
    async def send_message(self,message):
        contain_url = await check_url.check_url(self.reply_text)
        if contain_url and self.reply_text != "":
            await text2image.text_to_image(text=self.reply_text, font_path=self.sys_path + "/static/"+self.config['system']['font'],
                                           font_size=32, image_format='png', sys_path=self.sys_path)
            await self.api.post_message(channel_id=message.channel_id, file_image=self.sys_path + "/static/output.png",
                                        content="<@" + message.author.id + ">", msg_id=message.id)
        else:
            try:
                await self.api.post_message(channel_id=message.channel_id,
                                            content="<@" + message.author.id + ">" + self.reply_text, msg_id=message.id)
            except Exception as e:
                print(e)
                await text2image.text_to_image(text=self.reply_text,
                                               font_path=self.sys_path + "/static/" + self.config['system']['font'], font_size=32,
                                               image_format='png', sys_path=self.sys_path)
                await self.api.post_message(channel_id=message.channel_id,
                                            file_image=self.sys_path + "/static/output.png",
                                            content="<@" + message.author.id + ">", msg_id=message.id)
    def chat_with_gemini(self, message, text):
        response = None
        if not message.attachments:
            self.gemini_history['contents'].append({"parts": [{"text": text}], "role": "user"})
            response = gemini.chat_multi_turn(history=self.gemini_history, config=self.config,
                                              gemini_settings=self.gemini_settings)
        else:
            attachment_type = message.attachments[0].content_type
            if attachment_type.startswith("image/"):
                url = "https://" + message.attachments[0].url
                response = gemini.chat_text_and_image(url, text, self.config, self.gemini_settings)
            else:
                self.reply_text = "不支持的附件类型"
        if response:
            if response.status_code == 200:
                result = ast.literal_eval(response.text)
                if 'candidates' in result:
                    if not message.attachments:
                        self.gemini_history["contents"].append(result['candidates'][0]['content'])
                    self.reply_text = result['candidates'][0]['content']['parts'][0]['text']
                else:
                    self.reply_text = self.config['system']['error'] + "[AI未回复消息，原因：" + \
                                      result['promptFeedback']['blockReason'] + "]"
            else:
                self.reply_text = self.config['system']['error'] + "[错误码：" + response.status_code + "]"
        else:
            print(response.text)
    def chat_with_chatgpt(self, message, text):
        if not message.attachments:
            self.chatgpt_history.append({"role": "user", "content": text})
            response = gpt.chat_text_only(self.chatgpt_history, self.config, self.chatgpt_settings)
            ChatCompletionMessage = response.choices[0].message
            self.chatgpt_history.append({'role': ChatCompletionMessage.role, 'content': ChatCompletionMessage.content})
            self.reply_text = ChatCompletionMessage.content
        else:
            self.reply_text = "暂不支持读取附件哦"

    def chat_with_qwen(self,message, text):
        if not message.attachments:
            self.qwen_history.append({"role": "user", "content": text})
            response = qwen.chat_text_only(self.qwen_history, self.config, self.qwen_settings)
            ChatCompletionMessage = response.output.choices[0].message
            self.qwen_history.append({'role': ChatCompletionMessage.role, 'content': ChatCompletionMessage.content})
            self.reply_text = ChatCompletionMessage.content
        else:
            self.reply_text = "暂不支持读取附件哦"

    async def on_at_message_create(self, message: Message):
        print(message)
        self.reply_text =""
        text = message.content[0:message.content.find("<@!")] + message.content[
                                                                message.content.find(">", 9) + 1:].lstrip()
        if text == "/help":
            self.reply_text = self.help
        elif text == "/gemini":
            self.chatbot = gemini
            self.reply_text = '已切换至[gemini]'
        elif text == "/gpt":
            self.chatbot = gpt
            self.reply_text = '已切换至[chatgpt]'
        elif text == "/qwen":
            self.chatbot = qwen
            self.reply_text = '已切换至[通义千问]'
        elif text == "/reset":
            self.gemini_history = []
            self.chatgpt_history = [{"role": "system", "content": self.chatgpt_settings['preset']}]
            self.reply_text = '历史记录已清空'
        else:
            if self.chatbot == gemini:
                self.chat_with_gemini(message, text)
            elif self.chatbot == gpt:
                self.chat_with_chatgpt(message, text)
            elif self.chatbot == qwen:
                self.chat_with_qwen(message, text)
        await self.send_message(message)
