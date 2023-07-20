import boto3
from boto3.dynamodb.conditions import Key


def QueryDynamoDBTable(tableName, key, value):
    dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-1")
    table = dynamodb.Table(tableName)
    response = table.query(KeyConditionExpression=Key(key).eq(value))
    print(response['Items'])
    return response['Items']

QueryDynamoDBTable("animal-kingdom", "name", "shiba")