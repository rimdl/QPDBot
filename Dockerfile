python:3.10
WORKDIR /app  
COPY . /app  
VOLUME /app/config
RUN pip install -U pip
RUN pip install -r requirements.txt  
CMD ["python","main.py"]