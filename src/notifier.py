import boto3


class Notifier:
    def __init__(self, sns_client: boto3.client = None) -> None:
        self.sns_client = sns_client or boto3.client("sns")

    def publish(self, topic: str, message: str):
        self.sns_client.publish(
            TopicArn=topic, Subject="Volleyball Fixture Notifier", Message=message
        )
