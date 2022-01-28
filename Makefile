
.PHONY: all build


all: build push


build:
	docker build -t quay.io/bthomass/web-hook-bus-forwarder:latest .

build-dev:
	docker build -f Dockerfile.dev -t quay.io/bthomass/web-hook-bus-forwarder:dev .


push:
	docker push quay.io/bthomass/web-hook-bus-forwarder:latest

run:
	docker run -p 80:80 -p 443:443 --env-file env quay.io/bthomass/web-hook-bus-forwarder:latest

run-dev:
	docker run -p 8000:8000 --env-file env quay.io/bthomass/web-hook-bus-forwarder:dev

shell:
	docker run -it quay.io/bthomass/web-hook-bus-forwarder:latest  /bin/bash

shell-dev:
	docker run -it quay.io/bthomass/web-hook-bus-forwarder:dev  /bin/bash
