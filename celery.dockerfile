FROM python:3.6

COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .

ENTRYPOINT [ "/bin/sh" ]
CMD [ "./docker.celery.sh" ]