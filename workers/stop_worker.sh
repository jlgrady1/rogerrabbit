#!/bin/bash
ID=$1
APP_DEPLOY_DIR=/home/worker
BROKER_HOST_ID=$ID
LOG_DIR=/var/log
WORKER_ID="worker$ID"
BROKER_HOST=docker
cd $APP_DEPLOY_DIR
QUEUES='queue0,queue1,queue2,queue3,queue4,queue5,queue6,queue7'
MAX_TASKS=3
PID_PATH=/tmp/$WORKER_ID.pid
LOG_PATH=$LOG_DIR/$WORKER_ID.log


RABBIT_HOST=$BROKER_HOST # celery worker -n $WORKER_ID.%h -Q $QUEUES --pidfile=$PID_PATH --maxtasksperchild=$MAX_TASKS >> $LOG_PATH 2>&1
celery multi stopwait $WORKER_ID --pidfile=$PID_PATH
