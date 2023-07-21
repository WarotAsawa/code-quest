import boto3
from boto3.dynamodb.conditions import Key

#Function to Query DynamoDB Table
#Input: Table Name, Key, Value
#Output: List of Items
