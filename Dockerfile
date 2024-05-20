FROM alpine:latest  
WORKDIR /app  
COPY ./dist /app  
VOLUME /app/config
RUN chmod +x QPDBot
CMD ["./QPDBot"]
