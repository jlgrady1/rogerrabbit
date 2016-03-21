FROM rogerdeps:latest

ENV C_FORCE_ROOT=true
ENV DIP=172.16.5.146
RUN mkdir /worker
COPY celery/configure.sh .

RUN bash configure.sh
COPY workers/ /home/worker/
COPY celery/worker.sh /home/worker/
COPY celery/worker*.conf /etc/init/
RUN chown -R worker:worker /home/worker
RUN pip install -U pip
RUN pip install -r /home/worker/requirements.txt
WORKDIR /home/worker