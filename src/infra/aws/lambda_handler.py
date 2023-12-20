import os

import boto3
from aws_lambda_typing.context import Context
from aws_lambda_typing.events import SNSEvent

from src.message_generator import MessageGenerator
from src.notifier import Notifier
from src.utils.logger import get_logger

logger = get_logger()

TEAM_NAME = "TICKLE"

notifier = Notifier(sns_client=boto3.client("sns"))
message_generator = MessageGenerator()


def run(event: SNSEvent, context: Context) -> None:
    message = message_generator.generate_message(team_name=TEAM_NAME)
    logger.info(f"Message: {message}")
    notifier.publish(topic=os.environ["SNS_EMAIL_TOPIC"], message=message)
    logger.info("Successfully published message to email.")
