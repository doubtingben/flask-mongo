FROM python:3.5-alpine

RUN apk update
RUN apk add bash ca-certificates
RUN update-ca-certificates
RUN pip install --upgrade pip
RUN pip install Flask flask-login flask-script WTForms mongoengine flask_mongoengine

ADD code /code

EXPOSE 5000

ENTRYPOINT ["python", "/code/manage.py", "runserver"]
