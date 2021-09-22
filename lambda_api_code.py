import json
import re


def respond(response, code):
    return {
            'statusCode': code,
            'body': json.dumps(response)
        }


def bday_wish(name):
    return "Happy Birthday, {}!".format(name)


def lambda_handler(event, context):
    body = json.loads(event["body"])
    name = body['name']
    
    if bool(re.match('[a-zA-Z\s]+$', name)):
        response_string = bday_wish(name)
        return respond(response_string, 200)
    else:
        return respond(None, 400)
  