import json
from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths

logger = Logger()

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def handler(event, context):
    logger.info(event)

    return {
      'statusCode': 200,
      'body': json.dumps({}),
      'headers': {'Content-Type': 'application/json'}
    }
