
.PHONY: all build

IMAGE=quay.io/bthomass/acme-flask:latest


all: build push


build:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -p 80:80 -p 443:443 --env-file env $(IMAGE)

shell:
	docker run -it $(IMAGE) /bin/bash
