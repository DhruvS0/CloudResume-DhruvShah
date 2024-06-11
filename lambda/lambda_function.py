import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count')

def lambda_handler(event, context):
    response = table.get_item(Key={'id': 'counter'})
    count = response.get('Item', {}).get('count', 0) + 1
    table.put_item(Item={'id': 'counter', 'count': count})
    return {
        'statusCode': 200,
        'body': json.dumps({'count': count})
    }
