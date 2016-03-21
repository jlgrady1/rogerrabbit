
import logging
from celery.utils.log import get_task_logger
from time import sleep
from celery_tasks import normal_priority
from subprocess import check_output
task = normal_priority.task

log = get_task_logger(__name__)
logging.basicConfig(filename='/var/log/celery/worker.log', level=logging.DEBUG)


def _log_it(output, file='/var/log/celery/worker.log'):
    try:
        cmd = 'echo "{}" >> {}'.format(output, file)
        check_output(cmd, shell=True)
    except:
        pass


@task(ignore_result=True)
def test_sleep(i=0):
    sleep(5)
    msg = "Completed task test_sleep with int {}".format(i)
    log.info(msg)
    _log_it(msg)
