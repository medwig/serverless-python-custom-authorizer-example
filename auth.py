""""
A lambda custom authorizer for API KEY tokens.
A very basic implementation that checks a hardcoded api key.
"""

ACCESS_TOKEN = "123abc"


def generate_policy(effect, methodArn):
    """The auth lambda needs to return this AWS policy document to API Gateway
    """
    principalId = "userid|placeholder"  # this would be obtained from db lookup of the api key
    policyDocument = {
        "Version": "2012-10-17",
        "Statement": [
            {"Action": "execute-api:Invoke", "Effect": effect, "Resource": methodArn}
        ],
    }
    authResponse = {"principalId": principalId, "policyDocument": policyDocument}
    return authResponse


def handler(event, context):
    """Handler of the custom auth lambda. This will receive an event from API Gateway in the form:
        {'type': 'TOKEN', 'methodArn': 'arn:aws:execute-api:...', 'authorizationToken': 'Bearer 123abc'}
    """
    # Check if token is a valid api key
    token = event["authorizationToken"].split()[1]
    if token == ACCESS_TOKEN:
        return generate_policy('Allow', event["methodArn"])

    return generate_policy('Deny', event["methodArn"])
