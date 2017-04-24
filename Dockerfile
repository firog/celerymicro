FROM python:alpine
MAINTAINER Olof Markstedt <olofmarkstedt@gmail.com>

COPY . .
RUN pip install -r requirements.txt
CMD touch celery.log
CMD touch celery.pid

CMD ["./run.sh"]
#ENV C_FORCE_ROOT 1
#CMD ["celery multi start worker1 -A celery_worker.celery --broker=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672//"]
