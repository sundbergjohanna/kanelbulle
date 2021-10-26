FROM python:3.8-slim
COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD . /worker
WORKDIR /worker
ENTRYPOINT celery -A cel worker --loglevel=info
