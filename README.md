# hello.icinga2

Playing around with [Icinga2](https://github.com/Icinga/icinga2) on [Open Container Platform (OCP)](https://www.openshift.com/).

## Usage

```console
docker-compose up -d
curl -v -k -u "icinga2-director:api123" -H "Accept: application/json" https://localhost:5665/v1
docker-compose down
```

## OCP

Create build config template

```console
cd icinga2
oc new-build . --strategy=docker -o yaml > ..\ocp\build-config.yml
```

and tweak `git.uri` and  `strategy.dockerStrategy.dockerfilePath`:

```yml
    ...
   source:
      git:
        ref: master
        uri: https://github.com/mkoertgen/hello.icinga2.git
      type: Git
    strategy:
      dockerStrategy:
        dockerfilePath: ./icinga2/Dockerfile    ...
```

Next create the build configuration from the template

```console
oc create -f ocp\build-config.yml
# oc start-build helloicinga2
```
