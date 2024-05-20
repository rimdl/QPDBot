FROM alpine:latest  
WORKDIR /app  
COPY . /app  
VOLUME /app/config
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install -r requirements.txt
CMD ["python","main.py"]
