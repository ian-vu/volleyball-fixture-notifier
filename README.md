![CI](https://github.com/ian-vu/volleyball-fixture-notifier/actions/workflows/ci.yml/badge.svg)

# Volleyball Fixture Notifier

This service is a weekly automation that will send a team's volleyball fixture time weekly.

## Set up

```commandline
make setup-all
```

**Install serverless**

```commandline
npm install -g serverless
```

## How to run

See makefile otherwise:

```commandline
python -m scripts.print_volleyball_team_fixture
```