import aws_cdk as core
import aws_cdk.assertions as assertions

from api_test.api_test_stack import ApiTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_test/api_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiTestStack(app, "api-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
