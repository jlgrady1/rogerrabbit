"""
Define the celery apps which can be used to create
tasks which are sent to different broker hosts.

The pattern is to create a loader class that returns a particular
configuration module.

"""
from celery import Celery
from celery.loaders.base import BaseLoader
from celery.datastructures import DictAttribute


class NormalPriorityLoader(BaseLoader):
    def read_configuration(self, module_path='celeryconfig'):
        usercfg = self._import_config_module(module_path)
        return DictAttribute(usercfg)

normal_priority = Celery(loader=NormalPriorityLoader)
_pyflakes = normal_priority

__all__ = [
    'normal_priority',
    'NormalPriorityLoader',
]
