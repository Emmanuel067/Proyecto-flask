FROM python:3
MAINTAINER emmanuel0xff
RUN mkdir -p /opt/services/flaskapp/src
COPY requirements.txt /opt/services/flaskapp/src
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
EXPOSE 8080
CMD ["python", "server.py"]