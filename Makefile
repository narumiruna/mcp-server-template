all: format lint type test

format:
	uv run ruff format .

lint:
	uv run ruff check .

type:
	uv run ty check .

test:
	uv run pytest -v -s --cov=src tests

publish:
	uv build -f wheel
	uv publish

.PHONY: format lint type test publish
