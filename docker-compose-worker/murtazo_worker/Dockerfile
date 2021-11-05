FROM quay.io/fenicsproject/stable:current
USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install celery
RUN pip3 install pymongo

ADD . /murtazo_worker/
WORKDIR /murtazo_worker/
RUN chmod 755 ./navier_stokes_solver/airfoil
ENTRYPOINT celery -A cel_mur worker --concurrency=1 --loglevel=info
