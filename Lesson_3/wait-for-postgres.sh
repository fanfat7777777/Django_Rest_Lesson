#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="123" psql -h "$host" -d "db" -U "nikolay" -c '\q'; do
    >&2 echo "Postgress is unavailable - sleeping"
    sleep 1
done

>&2 echo "Posgres is up - executing command"
exec $cmd