img=duckietown/aido1_test_amod-evaluator:latest


all: push

push: build
	docker push $(img)

build:
	docker build -t $(img) .

build-no-cache:
	docker build -t $(img) . --no-cache


define-challenge:
	dts challenges define --config ../challenge.yaml --build aido-host:.

define-challenge-no-cache:
	dts challenges define --config ../challenge.yaml --build aido-host:. --no-cache
