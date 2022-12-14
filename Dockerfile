FROM python:3.9-slim
  
WORKDIR app/src

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./
CMD ["uvicorn","app:app","--port","3002","--host","0.0.0.0"]