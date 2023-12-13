FROM python:3 
MAINTAINER israOxff <root@isra0xff.me>

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/flaskapp/src
COPY requirements.txt /opt/services/flaskapp/src
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
EXPOSE 9796
CMD ["python", "server.py"]
