PHONY: down build up


DOCKER_COMPOSE_CMD = docker compose

down:
	${DOCKER_COMPOSE_CMD} down -v --remove-orphans

build:
	DOCKER_BUILDKIT=1 ${DOCKER_COMPOSE_CMD} build

up:
	${DOCKER_COMPOSE_CMD} up