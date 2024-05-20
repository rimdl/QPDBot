FROM alpine:latest  
WORKDIR /app  
COPY ./dist /app  
VOLUME /app/config
RUN apk add python3
RUN apk add py3-pip
RUN chmod +x QPDBot
CMD ["./QPDBot"]
