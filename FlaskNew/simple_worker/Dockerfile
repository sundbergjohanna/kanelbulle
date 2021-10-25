FROM quay.io/fenicsproject/stable:current


USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
#RUN pip3 install celery
#RUN pip3 install numpy
RUN apt-get install -y gmsh

#RUN apt-get install -y python-numpy
#RUN apt-get install -y python-gmsh
#RUN pip3 install --upgrade pip

#USER root
#RUN apt-get -qq update && \
#    apt-get -y upgrade && \
#    apt-get -y install python3-scipy && \
#    apt-get install -y python3-dolfin && \
#    apt-get -y install build-essential cmake && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
#USER root

#RUN apt-get update && \
#    apt-get -y upgrade && \
#    apt-get -y install python3-scipy && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
#    apt-get -y install python-gmsh


# layer caching for faster builds
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

#COPY app.py /app.py
ADD . /simple_worker
WORKDIR /simple_worker
RUN chmod +x unpack_murtazo.sh
RUN ./unpack_murtazo.sh
RUN chmod +x second_step.sh
RUN ./second_step.sh

ENTRYPOINT celery -A tasks worker --loglevel=info
#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']
