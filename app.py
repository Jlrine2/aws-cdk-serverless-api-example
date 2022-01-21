#!/usr/bin/env python3
import os

import aws_cdk as cdk

from api_test.api_test_stack import ApiTestStack


app = cdk.App()
ApiTestStack(app, "ApiTestStack",)

app.synth()
