import boto3

awsResource = boto3.resource("s3") # S3 bucket obj
bucket = awsResource.Bucket("boto3pract1xxxddd") #giving the bucket a name

#create bucket
response = bucket.create(
    ACL='private',
)

print(response)