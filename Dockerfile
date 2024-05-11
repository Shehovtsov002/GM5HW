FROM python:3.12

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/