import json
from aws_lambda_powertools import Logger

logger = Logger()

@logger.inject_lambda_context
def handler(event, context):
    logger.info(event)

    return {
      'statusCode': 200,
      'body': json.dumps({}),
      'headers': {'Content-Type': 'application/json'}
    }
