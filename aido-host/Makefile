img=duckietown/aido1_amod1-aidohost:latest


all: push

push: build
	docker push $(img)

build:
	docker build --pull -t $(img) .

build-no-cache:
	docker build --pull -t $(img) . --no-cache

