from celery import Celery
from celery.utils.log import get_task_logger
from time import sleep

celery = Celery('tasks', broker='amqp://guest:guest@127.0.0.1:5672//')
celery_log = get_task_logger(__name__)


class CeleryConfig:
    task_serializer = "pickle"
    result_serializer = "pickle"
    event_serializer = "json"
    accept_content = ["application/json", "application/x-python-serialize"]
    result_accept_content = ["application/json", "application/x-python-serialize"]


celery.config_from_object(CeleryConfig)


@celery.task
def create_bring_label(bring_order: BringOrder):
    sleep(10)
    celery_log.info(f"Order Complete!")
    return {"Bring label to create": bring_order}
