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
