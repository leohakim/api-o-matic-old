.ONESHELL:

lint:
	prospector

mypy:
	docker exec -ti mypy api_o_matic

test:
	python -m unittest

cov:
	coverage run -m unittest
	coverage report
	coverage html
