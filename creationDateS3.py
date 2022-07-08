# we will be using our public S3 Bucket that we created "boto3pract1"

import boto3

def findBucketInfo():
    # create low lvl service client by name
    s3Resource = boto3.client("s3")
    print(s3Resource)
    
    print()
    
    # how many buckets creted
    howMany = s3Resource.list_buckets()
    
    # since I have mult buckets I'll target the bucket I want using the index
    howManyBuckets = s3Resource.list_buckets() ["Buckets"] [0] 
    
    #Name of bucket I'm targeting
    howManyBucketsName = s3Resource.list_buckets() ["Buckets"] [0] ["Name"]
    
    # Creation date of bucket that I'm looking for
    howManyBucketsCreation = s3Resource.list_buckets() ["Buckets"] [0] ["CreationDate"]
    dateCreated = howManyBucketsCreation.strftime("%m-%d-%Y")
    
    # print(howMany)
    print("Bucket info that I'm looking for:")
    print(howManyBuckets)
    print()
    print("Name of bucket I want: " + howManyBucketsName)
    print()
    print("Creation Date:", dateCreated)
    
findBucketInfo()