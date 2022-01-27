
.PHONY: all build copy


all: build push


build: copy
	docker build -t quay.io/bthomass/web-hook-bus-forwarder:latest .


push:
	docker push quay.io/bthomass/web-hook-bus-forwarder:latest

run:
	docker run -p 80:80 -p 443:443 --env-file env quay.io/bthomass/web-hook-bus-forwarder:latest

shell:
	docker run -it quay.io/bthomass/web-hook-bus-forwarder:latest  /bin/bash
