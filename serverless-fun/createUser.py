import boto3
import os
import uuid

def lambda_handler(event, context):
    
    recordId = str(uuid.uuid4())
    username = event["username"]

    print('Creating new user:  ' + username)

    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['USER_TABLE_NAME'])
    table.put_item(
        Item={
            'id' : recordId,
            'username' : username
        }
    )
