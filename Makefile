DOCKER_COMPOSE_COMMAND := $(shell command -v docker-compose 2> /dev/null || echo "docker compose")

.PHONY: add-lib
add-lib:
	poetry add $(filter-out $@,$(MAKECMDGOALS))


.PHONY: add-lib-dev
add-lib-dev:
	poetry add $(filter-out $@,$(MAKECMDGOALS)) --group dev

.PHONY: add-roles
add-roles:
	poetry run python -m src.manage add_default_roles src/accounts/permissions.json

.PHONY: del-add-dummy
del-add-dummy:
	poetry run python -m src.manage add-dummy-data --delete

.PHONY: add-dummy
add-dummy:
	poetry run python -m src.manage add-dummy-data

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m src.manage makemigrations

.PHONY: run-celery
run-celery:
	poetry run celery -A src.project worker -l INFO

.PHONY: run-dependencies
run-dependencies:
	test -f .env || touch .env
	${DOCKER_COMPOSE_COMMAND} -f docker-compose.dev.yml up --force-recreate db redis

.PHONY: run-email-server
run-email-server:
	poetry run python -m aiosmtpd -n -l localhost:8025

.PHONY: run-server
run-server:
	poetry run python -m src.manage runserver

.PHONY: shell
shell:
	poetry run python -m src.manage shell

.PHONY: superuser
superuser:
	poetry run python -m src.manage createsuperuser

.PHONY: translate
translate:
	poetry run python -m src.manage makemessages --all
	poetry run python -m src.manage compilemessages

.PHONY: update
update: install migrate install-pre-commit ;