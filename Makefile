
all:


define-challenge:
	dts challenges define --config challenge.yaml --build aido-host:aido-host,aido-scorer:aido-scorer

define-challenge-no-cache:
	dts challenges define --config challenge.yaml --build aido-host:aido-host,aido-scorer:aido-scorer --no-cache
