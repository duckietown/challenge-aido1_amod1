
all:

test:
	rm -rf out-challenges
	docker-compose down -v
	docker-compose build --pull
	docker-compose up --build


define-challenge:

	dts challenges define --config efficiency.challenge.yaml
	dts challenges define --config service_quality.challenge.yaml
	dts challenges define --config fleet_size.challenge.yaml

define-challenge-no-cache:
	# only no-cache for the first - they are the same image
	dts challenges define --no-cache  --config efficiency.challenge.yaml
	dts challenges define    --config service_quality.challenge.yaml
	dts challenges define    --config fleet_size.challenge.yaml
