import json


def main(event, context):
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

        result = value_1 + value_2

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
    except Exception as e:
        return {
            "statusCode": 567,
            "body": json.dumps('Something went wrong')
        }
