format:
	uv run ruff format .

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix

type:
	uv run mypy --install-types --non-interactive .

mcp:
	uv run fastmcp run --server-spec mcp.json

#test:
#	uv run pytest -v -s --cov=src tests

#publish:
#	uv build -f wheel
#	uv publish

run:
	uv run chainlit run main.py

.PHONY: format lint fix type test publish
