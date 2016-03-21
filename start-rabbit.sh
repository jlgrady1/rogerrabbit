#!/bin/bash
docker rm -f rogerrabbitmq
docker run -p 5672:5672 -p 15672:15672 -d --name rogerrabbitmq --hostname rogerrabbitmq rogerrabbit bash rabbit.sh