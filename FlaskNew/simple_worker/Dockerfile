FROM quay.io/fenicsproject/stable:current
FROM python:3.8

USER root
RUN apt-get -qq update && \
    apt-get -y upgrade && \
    apt-get -y install python3-scipy && \
    apt-get -y install build-essential cmake && \
    apt-get -y install python-dolfin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
USER root

#RUN apt-get update && \
#    apt-get -y upgrade && \
#    apt-get -y install python3-scipy && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
#    apt-get -y install python-gmsh


# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

#COPY app.py /app.py
ADD . /simple_worker
WORKDIR /simple_worker
RUN chmod +x unpack_murtazo.sh
RUN ./unpack_murtazo.sh

ENTRYPOINT celery -A tasks worker --loglevel=info
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
