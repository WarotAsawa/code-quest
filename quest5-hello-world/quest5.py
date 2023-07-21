import boto3

#Funtion to push a message to SNS
#Input: Topic and message
#Output: Response from SNS

def PushMessageToSNS(topic,message):
    sns = boto3.client('sns',region_name='ap-southeast-1')
    response = sns.publish(
        TopicArn=topic,
        Message=message,
        Subject='Hello World'
    )
    return response

topic = "arn:aws:sns:ap-southeast-1:638806779113:hello-world-topic"
message = "Hi There"

print(PushMessageToSNS(topic,message))
