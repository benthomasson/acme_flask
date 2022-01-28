#!/bin/bash

openssl genrsa 4096 > server/server.key
openssl genrsa 4096 > account.key
openssl req -new -sha256 -key server/server.key -subj "/CN=${FQDN}" > domain.csr
./acme_flask.py

gunicorn -w 4 -b 0.0.0.0:443 --certfile=acme/server.crt --keyfile=server/server.key forwarder:app

while :; do sleep 2073600; done

