#!/bin/sh -ex
celery -A food_stories worker --loglevel=info  &
celery -A food_stories beat --pidfile=  -l info -S django &
tail -f /dev/null
