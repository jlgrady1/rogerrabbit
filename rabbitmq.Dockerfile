FROM rogerdeps:latest
RUN mkdir /rabbit
WORKDIR /rabbit
RUN wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/rabbitmq_v3_5_6/bin/rabbitmqadmin --no-check-certificate && chmod +x rabbitmqadmin && cp rabbitmqadmin /usr/local/bin

COPY rabbit/* /rabbit/


EXPOSE 55672 5672