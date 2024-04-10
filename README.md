# 推荐优先查看文档 🍀
[文档✅](https://xinsis-organization.gitbook.io/qpdbot/)
# 👉关于QPDBot👈
> QQ频道机器人，可使用Chat GPT、gemini、qwen
- python >= 3.10
## 💽安装
```shell
pip install -r requirements.txt
```
## 📖配置
- 主要配置config目录下的config.yaml文件，具体查看文件内的说明，或者点击查看[📚about config](https://xinsis-organization.gitbook.io/qpdbot/qi-bu/guan-yu-config.yaml)

## 🏃‍♂️启动
```shell
python main.py
```

## 🍾docker
- 新建一个目录（例如命令中的`/path/to/config`），用于存放配置文件，下载本程序中的config文件夹下的三个文件，将相关配置设置好后，将其放置在你新建的目录下。
```shell
docker run --name=QPDBot -d -v /path/to/config:/app/config registry.cn-hangzhou.aliyuncs.com/xinsi_q/qpdbot:latest
```

## ⏰更新日志

|date|description|
|-|-|
|2023-11-20|创建项目，并添加了对chagpt、gemini的支持。|
|2024-02-08|添加对通义千问API的支持。|
|2024-4-10|可自行配置gemini的model，更换docker镜像地址|
