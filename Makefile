DOCKER_COMPOSE_COMMAND := $(shell command -v docker-compose 2> /dev/null || echo "docker compose")

.PHONY: add-lib
add-lib:
	poetry add $(filter-out $@,$(MAKECMDGOALS))


.PHONY: add-lib-dev
add-lib-dev:
	poetry add $(filter-out $@,$(MAKECMDGOALS)) --group dev

.PHONY: manage
manage:
	poetry run python -m src.manage $(filter-out $@,$(MAKECMDGOALS))

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

.PHONY: run-dependencies
run-dependencies:
	test -f .env || touch .env
	${DOCKER_COMPOSE_COMMAND} -f docker-compose.dev.yml up --force-recreate db redis

.PHONY: run-server
run-server:
	poetry run python -m src.manage runserver

.PHONY: shell
shell:
	poetry run python -m src.manage shell

.PHONY: superuser
superuser:
	poetry run python -m src.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit ;