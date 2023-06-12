#syntax=docker/dockerfile:1
FROM python:3.8-alpine

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN python3 database.py

ENV FLASK_APP=app.py
CMD ["flask", "run"]