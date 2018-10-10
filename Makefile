
all:

build:
	docker build aido-host
	docker build aido-scorer



define-challenge:
	dts challenges define --config challenge.yaml

define-challenge-no-cache:
	dts challenges define --config challenge.yaml   --no-cache
