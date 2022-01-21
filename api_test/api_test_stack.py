from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from python_constructs import python_lambda_api


class ApiTestStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        python_lambda_api.LambdaApiPython(
            self, "test-api",
            params=python_lambda_api.LambdaApiPythonParams(
                function_code_location='api_test/src/',
                function_index='api.py',
                function_handler='handler'
            )
        )
