FROM python:3.6-slim-stretch
MAINTAINER Filip Wallberg / filip@sdu.dk
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt install ffmpeg -y

RUN pip3 install --upgrade pip
RUN pip3 install setuptools pip --upgrade --force-reinstall
RUN pip3 install ffmpeg-normalize

ENV PYTHONHASHSEED=0
ENV PYTHONIOENCODING=utf-8

WORKDIR /app/
CMD [ "python3", "/app/hotfolder.py" ]