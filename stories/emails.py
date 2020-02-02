from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import *

def send_mail_to_subscribers():
    subscribers = list(Subscribe.objects.values_list('email', flat=True))
    stories = Story.objects.all()
    context = {
        'stories' : stories,
    }
    html = render_to_string('email-subscribers.html', context)
    send_mail(subject='Test', 
            message='Bu bir testdir', 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=subscribers, 
            html_message=html)