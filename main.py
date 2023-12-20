import yaml
import os
import sys
import QQBot
import botpy


sys_path = os.path.dirname(os.path.realpath(sys.argv[0]))
with open(sys_path + "/config/config.yaml", "r", encoding='utf-8') as file:
    config = yaml.load(file.read(), Loader=yaml.FullLoader)
with open(sys_path + "/config/gemini_settings.yaml", "r", encoding="utf-8") as file:
    gemini_settings = yaml.load(file.read(), Loader=yaml.FullLoader)
with open(sys_path + "/help.txt", "r", encoding="utf-8") as file:
    help = yaml.load(file.read(), Loader=yaml.FullLoader)
with open(sys_path + "/config/chatgpt_settings.yaml", "r", encoding='utf-8') as file:
    chatgpt_settings = yaml.load(file.read(), Loader=yaml.FullLoader)

bot = ""
if config['gemini']['api_key'] == "" and config['gpt']['api_key'] == "":
    print(">>AI未配置，请配置后启动程序！<<")
    sys.exit()
elif config['gemini']['api_key'] == "" and config['gpt']['api_key'] != "":
    print(">>gemini未配置，启动chatgpt<<")
    bot = "gpt"
elif config['gemini']['api_key'] != "" and config['gpt']['api_key'] == "":
    print(">>chatgpt未配置，启动gemini<<")
    bot = "gemini"
else:
    bot = config['system']['default_ai']
    print(">>AI已配置，默认启动"+bot+"<<")
intents = botpy.Intents(public_guild_messages=True)
client = QQBot.MyClient(intents=intents, bot=bot)
client.config = config
client.gemini_settings = gemini_settings
client.chatgpt_settings = chatgpt_settings
client.chatgpt_history = [{"role": "system", "content": chatgpt_settings['preset']}]
client.help = help
client.sys_path = sys_path
appid = config['QQBot']['appid']
token = config['QQBot']['token']
client.run(appid=appid, token=token)
