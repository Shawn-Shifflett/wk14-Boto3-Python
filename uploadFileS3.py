# uploading files to S3 Bucket

import boto3
import os
import glob

def upload():
    # upload file to the s2 bucket
    s3Resource = boto3.client("s3")
    s3Resource.upload_file(
        Filename = "textExample.txt",
        Bucket = "boto3pract1",
        Key = "textExample.txt"
        )
        
    # getting working dircet
    cwd = os.getcwd()
    print(cwd)
    
    cwd = cwd + "/upload/"
    print(cwd)
    
    #finding file
    files = glob.glob("*.py")
    print(files)

    

upload()