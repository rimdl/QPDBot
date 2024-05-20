FROM alpine:3.19  
WORKDIR /app  
COPY ./dist /app  
VOLUME /app/config
RUN chmod +x QPDBot 
CMD ["./QPDBot"]
