import json
from src.calc import add
from src.token_service import TokenService


def main(event, context):
    try:
        raw_headers = event["headers"]
        headers = json.loads(raw_headers)
        token = headers["Authorization"]
        TokenService(token).validate_token()
    except Exception as e:
        return {"status": 401, "body": json.dumps("Unauthorized")}

    try:
        raw_body = event['body']
        body = json.loads(raw_body)

        if 'value_1' not in body or 'value_2' not in body:
            return {
                "statusCode": 400,
                "body": json.dumps('Please provide 2 values to add')
            }

        value_1 = body['value_1']
        value_2 = body['value_2']

        result = add(value_1, value_2)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
    except Exception as e:
        return {
            "statusCode": 567,
            "body": json.dumps('Something went wrong')
        }
