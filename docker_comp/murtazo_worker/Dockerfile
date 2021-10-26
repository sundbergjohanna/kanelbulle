FROM quay.io/fenicsproject/stable:current
USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install celery

ADD . /murtazo_worker/
WORKDIR /murtazo_worker/

ENTRYPOINT celery -A cel_mur worker --loglevel=info
