setup:
	pip install -r requirements.txt

setup-dev:
	pip install -r dev-requirements.txt

setup-all: setup setup-dev

format-check:
	black --check .

format:
	black .

test-unit:
	pytest test/unit

test-all:
	pytest

run:
	python -m scripts.print_volleyball_team_fixture