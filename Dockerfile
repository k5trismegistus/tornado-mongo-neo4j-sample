FROM python:3.6-alpine3.7
WORKDIR /tmp
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app
WORKDIR /app
