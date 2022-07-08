# deleting obj in S3

import boto3
import os
import glob

def delete():
    s3Resource = boto3.client("s3")
    print(s3Resource)
    
    print()
    
    # delete single obj
    #obj = s3Resource.delete_object(
     #   Bucket = "boto3pract1",
      #  Key = "textExample.txt"
    #)
    #print(obj)
    
    # this will show all files inside the Bucket
        # this will only show 1 bc I deleted the other file already
    d = s3Resource.list_objects(Bucket = "boto3pract1")["Contents"]
    print("Content:")
    print(d)
    
    print(len(d))
    
    #deletes multiple files at once
    #for i in d:
     #   s3Resource.delete_object(
      #      Bucket = "boto3pract1", 
       #     Key = i["Key"]
        #    )
            
    #print(len(d))
    
delete()