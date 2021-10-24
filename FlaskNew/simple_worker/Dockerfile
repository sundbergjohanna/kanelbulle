FROM python:3.8-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN chmod +x first_step.sh
RUN ./first_step.sh

#COPY app.py /app.py
ADD . /simple_worker
WORKDIR /simple_worker

ENTRYPOINT celery -A tasks worker --loglevel=info
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
