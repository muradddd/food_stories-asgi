FROM python:3.6

COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .

CMD [ "daphne", "-b", "0.0.0.0", "-p", "8000", "food_stories.asgi:application"]