#!/bin/sh
#celery multi start worker1 -A tasks --broker=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672// -l info --pidfile="celery.pid" --logfile="celery.log"
#celery multi start worker1 -A tasks --broker=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672// -l info
celery -A tasks worker --loglevel=info --broker=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672//
#sleep 1
