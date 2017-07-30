import boto3
import os

def lambda_handler(event, context):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(os.environ['USER_TABLE_NAME'])

  response = table.scan()
  items = response['Items']

  return [entry[u'username'] for entry in items]