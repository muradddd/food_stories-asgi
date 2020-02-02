from django import template
from django.shortcuts import render
from stories.forms import (SubscribeForm, )

register = template.Library()

@register.inclusion_tag('includes/subscribe.html')
def subscribe_form(request):
   form = SubscribeForm
   return {'form': form}