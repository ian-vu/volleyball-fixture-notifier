from aws_lambda_typing.context import Context
from aws_lambda_typing.events import SNSEvent


def run(event: SNSEvent, context: Context) -> None:
    print("hello world")
