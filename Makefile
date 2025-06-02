install:
	uv sync

reinstall:
	uv sync
	uv build
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build
