FROM python:3.7.2 as build

WORKDIR /usr/src/app

COPY plugins/requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

COPY plugins/ .
RUN pylint *.py &&\
  coverage run -m unittest discover -v -s . -p *_test.py &&\
  coverage report -m

# cf.: https://github.com/jjethwa/icinga2
FROM jordan/icinga2:latest

### Add plugins
RUN apt-get update &&\
  apt-get install -y python3-pip &&\
  rm -rf /var/lib/apt/lists/

WORKDIR /opt/monitoring_plugins
ADD plugins/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD plugins/ .

