#!/bin/bash
set -e

if [ "$1" = 'icinga2' ]; then
  gosu icinga2 bash -c 'sudo -E /opt/run'
fi

exec "$@"
