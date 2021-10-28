FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD . /flask_app
WORKDIR /flask_app

ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0
