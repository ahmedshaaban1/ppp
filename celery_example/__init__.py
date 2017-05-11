from __future__ import absolute_import

from celery import Celery

app = Celery('fib',
             broker='amqp://guest:guest@localhost',
             backend='amqp://guest:guest@localhost',
             include=['celery_example.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_SEND_EVENTS=True,
    CELERY_SEND_TASK_SENT_EVENT=True
)
