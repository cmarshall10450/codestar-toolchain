import json
import datetime


def handler(event, context):
    data = {
        "name": event["name"],
        "email": event["email"]
    }

    print(event)

    return {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {'Content-Type': 'application/json'}
    }
