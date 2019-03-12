# cf.: https://github.com/jjethwa/icinga2
FROM jordan/icinga2:latest

# NOTE: We want to run in Open Caontainer Platform (OCP). By default SCC, containers must not be run as root, cf.:
# https://docs.openshift.com/enterprise/3.2/admin_guide/manage_scc.html#enable-dockerhub-images-that-require-root
# Dockerfile best practie, cf.: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN addgroup --system icinga2 &&\
  adduser --system icinga2 --ingroup icinga2 &&\
  usermod -aG sudo icinga2 &&\
  echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER icinga2

ENTRYPOINT [ "sudo", "-E", "/opt/run" ]
