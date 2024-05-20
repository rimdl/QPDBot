FROM alpine:3.18  
WORKDIR /app  
COPY ./dist /app  
VOLUME /app/config
RUN apk add glibc
RUN chmod +x QPDBot
CMD ["./QPDBot"]
