from aws_cdk import Stack, Duration
from aws_cdk.aws_lambda import DockerImageFunction, DockerImageCode
from constructs import Construct


class NotifierStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.lambda_ = self._create_lambda()

    def _create_lambda(self) -> DockerImageFunction:
        return DockerImageFunction(self, "lambda",
                                   timeout=Duration.seconds(15),
                                   code=DockerImageCode.from_image_asset(
                                       directory='../', file='./cdk/notifier/Dockerfile',
                                       exclude=['cdk.out']
                                   )
                                   )
