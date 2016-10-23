FROM python:3.5-alpine

RUN apk update
RUN apk add bash ca-certificates
RUN update-ca-certificates
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD code/ /code/

EXPOSE 5000

ENTRYPOINT ["python", "/code/manage.py", "runserver"]
