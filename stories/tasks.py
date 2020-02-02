from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .emails import (send_mail_to_subscribers, )


@shared_task(name='Send email to subscribers')
def send_mail_to_subscribers_task():
    send_mail_to_subscribers()


@shared_task(name='This is only a test', max_retries=3)
def say_hello():
    print('hello')
