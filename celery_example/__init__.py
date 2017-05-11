from __future__ import absolute_import

from celery import Celery

try:
    import boto3
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
                 {'Name': 'tag:Name', 'Values': ['master']}])

    host = list(instances)[0].public_ip_address

except:
    host = 'localhost'

app = Celery('fib',
             broker='amqp://guest:guest@{}'.format(host),
             backend='amqp://guest:guest@{}'.format(host),
             include=['celery_example.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_SEND_EVENTS=True,
    CELERY_SEND_TASK_SENT_EVENT=True
)
