from functools import cache

import boto3

from scripts.base_script import BaseScript


class SubscribeEmailToSnsTopic(BaseScript):
    """
    How to run:
        python -m scripts.subscribe_email_to_sns_topic --help
    """

    description = "Subscribe an email to SNS Topic that will be sent email."

    _STACK_NAME_PREFIX = "volleyball-fixture-notifier"

    def _get_stack_name(self, stage: str):
        return f"{self._STACK_NAME_PREFIX}-{stage}"

    def _extend_parser(self) -> None:
        """Override parent class method"""
        self._parser.add_argument(
            "-e",
            "--email",
            help="Email address to subscribe to SNS Topic which will receive notification.",
            required=True,
        )
        self._parser.add_argument(
            "-s",
            "--stage",
            help="Stage of serverless stack. This will determine which SNS topic to add subscription to.",
            required=True,
        )

    @cache
    def _get_sns_topic_arn(self):
        stage = self._args.stage
        cf_client = boto3.client("cloudformation")
        res = cf_client.describe_stacks(StackName=self._get_stack_name(stage))
        stack_outputs = res["Stacks"][0]["Outputs"]

        arn = next(
            output["OutputValue"]
            for output in stack_outputs
            if output["OutputKey"] == "snsEmailTopicArn"
        )

        return arn

    def run(self) -> None:
        arn = self._get_sns_topic_arn()

        res = boto3.client("sns").subscribe(
            Protocol="email", TopicArn=arn, Endpoint=self._args.email
        )

        assert res["ResponseMetadata"]["HTTPStatusCode"] == 200
        assert res["SubscriptionArn"] == "pending confirmation"

        print("Successful script run.")
        print(
            f"{self._args.email} is pending subscription to {self._get_sns_topic_arn()}. "
            f"Subscription email has been send to inbox.\nClick link in email to complete subscription!"
        )


if __name__ == "__main__":
    SubscribeEmailToSnsTopic().run()
