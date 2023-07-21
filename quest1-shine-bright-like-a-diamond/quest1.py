import boto3

#Function to ListFile From S3 Bucket
#Input: Bucket Name
#Output: List of File Name

def ListFileFromBucket(bucket):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    for file in bucket.objects.all():
        print(file.key)

#Function to Download File From S3 Bucket
#Input: Bucket Name, Key, Filename

def DownloadFileFromS3(bucket, key, filename):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(key, filename);

bucket = "cloudday-bkk-code-whisperer"
key = "quest1/st-diamond.jpeg"
filename = "./diamond.jpeg"

ListFileFromBucket(bucket);

DownloadFileFromS3(bucket, key, filename);