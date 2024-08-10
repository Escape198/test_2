#!/bin/sh

flask db upgrade
flask fab create-admin --username admin --firstname Admin --lastname Admin --email admin@example.com --password admin

exec "$@"
