import boto3

def ListFileFromBucket(bucket):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    for file in bucket.objects.all():
        print(file.key)

def DownloadFileFromS3(bucket, key, filename):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(key, filename);

bucket = "cloudday-bkk-code-whisperer"
key = "quest1/st-diamond.jpeg"
filename = "./diamond.jpeg"

ListFileFromBucket(bucket);

DownloadFileFromS3(bucket, key, filename);