FROM python:3.10  
WORKDIR /app  
COPY . /app  
VOLUME /app/config
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple  
RUN pip config set install.trusted-host mirrors.aliyun.com  
RUN pip install -U pip
RUN pip install -r requirements.txt  
CMD ["python","main.py"]
