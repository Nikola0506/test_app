#FROM python:3.9-slim
#MAINTAINER Trip app
#
#ENV PYTHONUNBUFFERED 1
#
#COPY ./requirements.txt /requirements.txt
#RUN pip install -r  /requirements.txt
#
#RUN mkdir /trip_app
#WORKDIR /trip_app
#COPY ./trip_app /trip_app
#
##RUN adduser -D user
##USER user

FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/