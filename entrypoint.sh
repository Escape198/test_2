#!/bin/sh

env

flask db upgrade

exec "$@"
