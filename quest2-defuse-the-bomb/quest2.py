import boto3

def GetSecret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    return get_secret_value_response['SecretString']


print(GetSecret("cloudday-bkk-defuser","ap-southeast-1"));