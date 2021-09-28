import json

def hello(event, context):
    body = {
        "message": "Hello Python 3!"
    }

    return {
        "body": json.dumps(body),
        "statusCode": 200,
    }


def nullresp(event, context):
    body = None

    return {
        "body": json.dumps(body),
        "statusCode": 200,
    }


def emptyresp(event, context):
    body = ""

    return {
        "body": json.dumps(body),
        "statusCode": 200,
    }
