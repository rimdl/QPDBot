FROM alpine:3.19  
WORKDIR /app  
COPY ./dist /app  
VOLUME /app/config
RUN ls
RUN chmod +x QPDBot
CMD ["ls","./app/QPDBot"]
