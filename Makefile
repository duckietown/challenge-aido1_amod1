
all:

build:
	docker build aido-host
	docker build aido-scorer



define-challenge:

	dts challenges define --config efficiency.challenge.yaml
	dts challenges define --config service_quality.challenge.yaml
	dts challenges define --config fleet_size.challenge.yaml

define-challenge-no-cache:
	dts challenges define --no-cache  --config efficiency.challenge.yaml
	dts challenges define --no-cache  --config service_quality.challenge.yaml
	dts challenges define --no-cache  --config fleet_size.challenge.yaml
