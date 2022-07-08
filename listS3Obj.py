# list in S3 

import boto3

def listt():
    s3Resource = boto3.client("s3")
    print(s3Resource)
    
    print()
    
    # get obj content list
    obj = s3Resource.list_objects(Bucket = "boto3pract1")["Contents"]
    print("Obects:")
    print(obj)
    
    # get length of obj in s3 bucket
    lenghtt = len(obj)
    
    if lenghtt > 0:
        print("There are", lenghtt, "objects")
    else:
        print("There's no objects")
        
    print()
        
    # get file names inside S3 Bucket
    print("Files in S3 Bucket:")
    for i in obj:
        print(i["Key"])


listt()