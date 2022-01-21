
.PHONY: all build copy


all: build push


build: copy
	docker build -t quay.io/bthomass/web-hook-bus-forwarder:latest .


push:
	docker push quay.io/bthomass/web-hook-bus-forwarder:latest

run:
	docker run -p 8000:8000 --env-file env quay.io/bthomass/web-hook-bus-forwarder:latest
