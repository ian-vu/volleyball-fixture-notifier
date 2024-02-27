setup:
	pip install -r requirements.txt

setup-dev:
	pip install pip-tools && pip install -r requirements-dev.txt && npm install -g serverless && npm install

setup-all: setup-dev setup

upgrade-dev:
	pip-compile requirements-dev.in --upgrade

upgrade:
	pip-compile requirements.in --upgrade

upgrade-all: upgrade-dev upgrade

format-check:
	black --check --extend-exclude=.venv .

format:
	black . --extend-exclude=.venv

test-unit:
	pytest test/unit

test-all:
	pytest

run:
	python -m scripts.print_volleyball_team_fixture