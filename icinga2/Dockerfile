# cf.: https://github.com/jjethwa/icinga2
FROM jordan/icinga2:latest

# NOTE: We want to run in Open Caontainer Platform (OCP). By default SCC, containers must not be run as root, cf.:
# - https://docs.openshift.com/enterprise/3.2/creating_images/guidelines.html#openshift-enterprise-specific-guidelines
# - https://docs.openshift.com/enterprise/3.2/admin_guide/manage_scc.html#enable-dockerhub-images-that-require-root
# - https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN addgroup --system icinga2 &&\
  adduser --system icinga2 --disabled-password --ingroup icinga2 &&\
  echo "icinga2:icinga2" | chpasswd &&\
  usermod -aG sudo icinga2 &&\
  echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

#USER icinga2
ADD ./docker-entrypoint.sh /

ENTRYPOINT [ "/docker-entrypoint.sh" ]
