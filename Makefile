.ONESHELL:

mypy:
	docker exec -ti django mypy api_o_matic

test:
	docker exec -ti django pytest

cov:
	docker exec -ti django coverage run -m pytest && docker exec -ti django coverage report -m

docs:
	docker exec -ti docs make apidocs

migrations:
	docker exec -ti django python manage.py makemigrations

migrate:
	docker exec -ti django python manage.py migrate

psql:
	docker exec -ti postgres psql api_o_matic -U NOSdhiNXhxPQGzZGesshjzrrHHQOTUua

superuser:
	docker exec -ti django python manage.py createsuperuser

up:
	docker-compose -f local.yml up

up-build-amd64:
	export DOCKER_DEFAULT_PLATFORM=linux/amd64; \
  	echo $$DOCKER_DEFAULT_PLATFORM;\
	docker-compose -f local.yml up --build

up-build:
	docker-compose -f local.yml up --build

down:
	docker-compose -f local.yml down --remove-orphans
