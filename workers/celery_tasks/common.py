"""
A collection of Celery configuration settings that can be used by multiple apps.

"""
import os

BROKER_POOL_LIMIT = 10

# Celeryd configuration
CELERYD_CONCURRENCY = 2
CELERYD_PREFETCH_MULTIPLIER = 64
CELERYD_HIJACK_ROOT_LOGGER = False
CELERY_REDIRECT_STDOUTS = False
CELERY_IGNORE_RESULT = True
CELERY_DEFAULT_DELIVERY_MODE = "persistent"
CELERY_MESSAGE_COMPRESSION = "gzip"

# Send events so that tools like `celeryev` work
CELERY_SEND_EVENTS = False

# Miscellaneous options
CELERY_ALWAYS_EAGER = False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_DISABLE_RATE_LIMITS = True

CELERY_DEFAULT_QUEUE = 'queue0'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = '0'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


def get_broker_host(default=os.environ.get('DIP', '172.16.5.146')):
    # Likely, we're sending tasks to a broker, and using the default broker
    # connection.
    return default
