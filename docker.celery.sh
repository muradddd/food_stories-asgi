#!/bin/sh -ex
celery -A food_stories worker --loglevel=info --pidfile= &
celery -A food_stories beat -l info -S django &
tail -f /dev/null
