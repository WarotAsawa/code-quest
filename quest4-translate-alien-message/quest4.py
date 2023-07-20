import boto3

def RunLambdaFuntion(function, payload):
    client = boto3.client('lambda', region_name='ap-southeast-1')
    response = client.invoke(
        FunctionName=function,
        Payload=payload
    )
    #return payload as text
    return response[u'Payload'].read().decode('utf-8')

payload = "{\"message\": \"aovmywo*~y*Mvyn*Nk*B~r7B\"}"
response = RunLambdaFuntion("alien-translator",payload);
print(response)

