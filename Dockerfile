FROM python:3.8
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=jquery_pooling:init_app

