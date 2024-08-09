#!/bin/bash

if [ "$FLASK_ENV" = "development" ]; then
  echo "Running in development mode"
  exec flask run --host=0.0.0.0
else
  echo "Running in production mode"
  exec flask run --host=0.0.0.0 --port=8080
fi
