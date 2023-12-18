import boto3

from scripts.BaseScript import BaseScript


class SubscribeEmailToSnsTopic(BaseScript):
    """
    How to run:
        python -m scripts.subscribe_email_to_sns_topic \
            --email <EMAIL> \
            --topic-arn <TOPIC_ARN>
    """

    description = "Subscribe an email to SNS Topic that will be sent email."

    def _extend_parser(self) -> None:
        """Override parent class method"""
        self._parser.add_argument("-e", "--email", required=True)
        self._parser.add_argument("-t", "--topic-arn", required=True)

    def run(self) -> None:
        sns_client = boto3.client("sns")

        res = sns_client.subscribe(
            Protocol="email", TopicArn=self._args.topic_arn, Endpoint=self._args.email
        )

        assert res["ResponseMetadata"]["HTTPStatusCode"] == 200
        assert res["SubscriptionArn"] == "pending confirmation"

        print("Successful script run.")
        print("Email is pending confirmation. Check email inbox!")


if __name__ == "__main__":
    SubscribeEmailToSnsTopic().run()
