import os

import boto3
from aws_lambda_typing.context import Context
from aws_lambda_typing.events import SNSEvent

from src.MessageGenerator import MessageGenerator
from src.Notifier import Notifier

TEAM_NAME = "TICKLE"

notifier = Notifier(sns_client=boto3.client("sns"))
message_generator = MessageGenerator()


def run(event: SNSEvent, context: Context) -> None:
    message = message_generator.generate_message(team_name=TEAM_NAME)
    notifier.publish(topic=os.environ["SNS_EMAIL_TOPIC"], message=message)

    print(message)
