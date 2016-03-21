FROM ubuntu:12.04

RUN apt-get update && apt-get install -y iputils-ping libpq-dev python python-dev python-m2crypto python-pip  sudo swig vim wget

RUN wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc --no-check-certificate && apt-key add rabbitmq-signing-key-public.asc && rm rabbitmq-signing-key-public.asc
RUN wget http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc --no-check-certificate && apt-key add erlang_solutions.asc && rm erlang_solutions.asc
RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' >> /etc/apt/sources.list
RUN echo 'deb http://packages.erlang-solutions.com/ubuntu precise contrib' >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y rabbitmq-server

RUN pip install -U pip
RUN pip install celery==3.1.16
