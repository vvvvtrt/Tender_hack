project_dir := .


.PHONY: db
db:
	docker compose -f docker/docker-compose.yaml up -d postgres

.PHONY: build
build:
	docker compose -f docker/docker-compose.yaml up -d --build

.PHONY: logs
logs:
	docker compose -f docker/docker-compose.yaml logs

.PHONY: up
down:
	docker compose -f docker/docker-compose.yaml up -d

.PHONY: down
down:
	docker compose -f docker/docker-compose.yaml down

.PHONY: run
run:
	uvicorn backend.main:app --reload --port 8000 --host 0.0.0.0