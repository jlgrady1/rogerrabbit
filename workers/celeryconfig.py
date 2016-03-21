from kombu import (
    Exchange,
    Queue,
)

from celery_tasks.common import (
    get_broker_host,

    # Celery defaults
    BROKER_POOL_LIMIT,
    CELERYD_CONCURRENCY,
    CELERYD_PREFETCH_MULTIPLIER,
    CELERYD_HIJACK_ROOT_LOGGER,
    CELERY_REDIRECT_STDOUTS,
    CELERY_IGNORE_RESULT,
    CELERY_DEFAULT_DELIVERY_MODE,
    CELERY_MESSAGE_COMPRESSION,
    CELERY_SEND_EVENTS,
    CELERY_ALWAYS_EAGER,
    CELERY_EAGER_PROPAGATES_EXCEPTIONS,
    CELERY_DISABLE_RATE_LIMITS,
    CELERY_DEFAULT_QUEUE,
    CELERY_DEFAULT_EXCHANGE_TYPE,
    CELERY_DEFAULT_ROUTING_KEY,
    CELERY_ACCEPT_CONTENT,
)
# Celery defaults
_pyflakes = BROKER_POOL_LIMIT
_pyflakes = CELERYD_CONCURRENCY
_pyflakes = CELERYD_PREFETCH_MULTIPLIER
_pyflakes = CELERYD_HIJACK_ROOT_LOGGER
_pyflakes = CELERY_REDIRECT_STDOUTS
_pyflakes = CELERY_IGNORE_RESULT
_pyflakes = CELERY_DEFAULT_DELIVERY_MODE
_pyflakes = CELERY_MESSAGE_COMPRESSION
_pyflakes = CELERY_SEND_EVENTS
_pyflakes = CELERY_ALWAYS_EAGER
_pyflakes = CELERY_EAGER_PROPAGATES_EXCEPTIONS
_pyflakes = CELERY_DISABLE_RATE_LIMITS
_pyflakes = CELERY_DEFAULT_QUEUE
_pyflakes = CELERY_DEFAULT_EXCHANGE_TYPE
_pyflakes = CELERY_DEFAULT_ROUTING_KEY
_pyflakes = CELERY_ACCEPT_CONTENT

from celery_tasks.routers import DefaultRouter

# These are the modules that we import into Celery.
CELERY_IMPORTS = (
    "bi.rogerrabbit.tasks"
)

# Broker settings
HOST = get_broker_host()

BROKER_URL = "amqp://%s:%s@%s:%d/%s" % (
    'kiip',
    'kiip',
    HOST,
    5672,
    'kiip')

# ##############################################################################
# ### Default Queue
# These are the Default queues for the Kiip App.
# NOTE/WARNING: these queues are tightly coupled to the way we deploy celery worker hosts
# confirm with ops before changing this value.
# Enable multiple queues for Kiip Default queues.
default_exchange = Exchange('default')

CELERY_QUEUES = (
    Queue('queue0', default_exchange, routing_key='0'),
    Queue('queue1', default_exchange, routing_key='1'),
    Queue('queue2', default_exchange, routing_key='2'),
    Queue('queue3', default_exchange, routing_key='3'),
    Queue('queue4', default_exchange, routing_key='4'),
    Queue('queue5', default_exchange, routing_key='5')
)

# Use a custom router for different priorities
CELERY_ROUTES = (DefaultRouter(),)
