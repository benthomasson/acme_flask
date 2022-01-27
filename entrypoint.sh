#!/bin/bash

gunicorn -w 4 -b 0.0.0.0:80 forwarder:app

gunicorn -w 4 -b 0.0.0.0:80 -b 0.0.0.0:443 --certfile=server.crt --keyfile=server.key forwarder:app
