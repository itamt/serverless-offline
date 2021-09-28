import json

def hello(event, context):
#     body = {
#         "message": "Hello Python 3!"
#     }
    body = None

    return {
        "body": json.dumps(body),
        "statusCode": 200,
    }


# def null(event, context):
#     body = None
#
#     return {
#         "body": json.dumps(body),
#         "statusCode": 200,
#     }
#
#
# def empty(event, context):
#     body = ""
#
#     return {
#         "body": json.dumps(body),
#         "statusCode": 200,
#     }
