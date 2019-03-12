# hello.icinga2

Playing around with [Icinga2](https://github.com/Icinga/icinga2) on [Open Container Platform (OCP)](https://www.openshift.com/).

## Usage

```console
docker-compose up -d
curl -v -k -u "icinga2-director:api123" -H "Accept: application/json" https://localhost:5665/v1
docker-compose down
```
