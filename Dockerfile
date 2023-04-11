

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /dole_test_app


WORKDIR /dole_test_app


ADD . /dole_test_app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD gunicorn seedtest.wsgi:application --bind 0.0.0.0:$PORT