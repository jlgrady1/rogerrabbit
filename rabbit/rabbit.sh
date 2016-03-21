#!/bin/bash
# Start the service
#service rabbitmq-server start


# Set up users/env
#rabbitmqctl add_user rabbit rabbit
#rabbitmqctl add_vhost myvhost
#rabbitmqctl set_user_tags rabbit administrator
#rabbitmqctl set_permissions -p myvhost rabbit ".*" ".*" ".*"
mkdir -p /etc/rabbitmq/rabbitmq.conf.d
/usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management --offline

service rabbitmq-server start
# rabbitmqadmin delcare user name=kiip password=kiip tags=administrator
rabbitmqadmin import rabbit.config
service rabbitmq-server stop

rabbitmq-server
