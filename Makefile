setup:
	pip install -r requirements.txt

setup-dev:
	pip install -r requirements.txt

setup-all: setup setup-dev

lint-check:
	ruff check .

lint-fix:
	ruff check --fix .
