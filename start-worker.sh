#!/bin/bash
NAME=`dhelper name worker`
docker run -it -h $NAME --name $NAME rogerworker bash