![CI](https://github.com/ian-vu/volleyball-fixture-notifier/actions/workflows/ci.yml/badge.svg)

# Volleyball Fixture Notifier

This service is a weekly automation that will send a team's volleyball fixture time weekly.

## Infrastructure

This service uses the Serverless framework to configure/manage/deploy/test infrastructure.
See `serverless.yml` for all the configuration.

## How it works

There is an AWS Event Cron schedule that is sent up that will invoke an AWS Lambda function.
The Lambda will then scrape the volleyball fixture page and send a message to an AWS SNS topic.
Any email subscription that is set up for that topic will be sent the message.

## CI/CD

Continuous integration and continious delivery is set up for this service using Github Actions.
To see configuration see `./github/workflows` folder.

## Set up

Ensure NPM and Python is installed in your preferred way (nvm, virtual environments etc.).

**Install serverless**

```commandline
npm install -g serverless
```

**Set up dependencies**

```commandline
make setup-all
```

## Scripts

There are two scripts written for this project.

### 1. Print Volleyball Fixture

This script will print a teams fixture for the week, similar to the scheduled Lambda function.

**How to run**

```commandline
python -m scripts.print_volleyball_team_fixture --help
```

### 2. Subscribe Email to SNS Topic

This script will subscribe an provided email to a deployed stack's SNS Topic.

**How to run**

```commandline
python -m scripts.subscribe_email_to_sns_topic --help
```

## Testing

There are numerous tests written for this project. Unit and Integration tests are writting using `pytest`.

An end to end (e2e) test is written as a bash script that will use the `serverless` cli to invoke a lambda function
expecting to see
certain logs.

**How to run pytest**

```commandline
pytest test
```

**How to run e2e test**

```commandline
bash ./test/e2e/e2e.sh <STAGE_OF_DEPLOYMENT_TO_TEST>
```

## Useful manual commands

**Deploy a stack/stage**

```commandline
serverless deploy --verbose --stage <STAGE>
```

**Invoke Lambda function**

```commandline
serverless invoke --function cronHandler --stage <STAGE> --log
```