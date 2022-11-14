FROM python:3.7-slim-buster AS base

FROM base AS compiler

RUN echo "This is A test for github actions workflow"

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential default-libmysqlclient-dev 
    
RUN pip install django

FROM base AS builder

RUN apt-get update && apt-get install -y libgomp1 libaio1  wget unzip
WORKDIR    /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && \
    rm -f instantclient-basiclite-linuxx64.zip && \
    cd instantclient* && \
    rm -f *jdbc* *occi* *mysql* *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig
RUN python -m pip install cx_Oracle
RUN echo "exit" >> /root/.bashrc

RUN mkdir -p /src/api
# adding django project, always called client_api
ADD ./TheTrainApp /src/api/ 
RUN ls /src/api

EXPOSE 9005
WORKDIR /src/api

# running the project on 9005 port which was exposed earlier
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:9005"]
