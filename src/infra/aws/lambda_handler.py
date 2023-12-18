from aws_lambda_typing.context import Context
from aws_lambda_typing.events import SNSEvent

from src.MessageGenerator import MessageGenerator

TEAM_NAME = "TICKLE"


def run(event: SNSEvent, context: Context) -> None:
    message = MessageGenerator().generate_message(team_name=TEAM_NAME)

    print(message)
