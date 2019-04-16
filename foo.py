import json


def handler(event, context):
    result = {"it": "worked!"}
    return {"statusCode": 200, "body": json.dumps(result)}
