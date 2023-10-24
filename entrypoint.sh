#!/bin/bash

FQDN=example.com
mkdir -p server acme challenges
openssl genrsa 4096 > server/server.key
openssl genrsa 4096 > account.key
openssl req -new -sha256 -key server/server.key -subj "/CN=${FQDN}" > domain.csr
./acme_flask.py

gunicorn -w 4 -b 0.0.0.0:443 --certfile=acme/server.crt --keyfile=server/server.key hello:app

while :; do sleep 2073600; done

