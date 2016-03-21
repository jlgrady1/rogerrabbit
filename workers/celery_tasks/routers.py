import random


class DefaultRouter(object):
    def route_for_task(self, task, args=None, kwargs=None):
        num = random.randint(0, 5)
        return {
            'queue': 'queue%d' % num,
            'routing_key': '%d' % num
        }
