FROM python:3.7.2 as build

WORKDIR /usr/src/app

COPY plugins/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY plugins/ .
RUN pylint *.py &&\
  coverage run -m unittest discover -v -s . -p *_test.py &&\
  coverage report -m

# cf.: https://github.com/jjethwa/icinga2
FROM jordan/icinga2:latest

#ADD content/ /

# NOTE: We want to run in Open Caontainer Platform (OCP). By default SCC, containers must not be run as root, cf.:
# - https://docs.openshift.com/enterprise/3.2/creating_images/guidelines.html#openshift-enterprise-specific-guidelines
# - https://docs.openshift.com/enterprise/3.2/admin_guide/manage_scc.html#enable-dockerhub-images-that-require-root
# - https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN addgroup --system icinga2 &&\
  adduser --system icinga2 --disabled-password --ingroup icinga2 &&\
  echo "icinga2:icinga2" | chpasswd &&\
  usermod -aG sudo icinga2 &&\
  echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

### Add plugins
RUN apt-get update &&\
  apt-get install -y python3-pip dos2unix &&\
  rm -rf /var/lib/apt/lists/

USER icinga2

WORKDIR /opt/monitoring_plugins
ADD plugins/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD plugins/ .
RUN sudo dos2unix *.py

