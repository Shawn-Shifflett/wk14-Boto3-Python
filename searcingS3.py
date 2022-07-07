import boto3

resource = boto3.resource("s3")
# print what type of service
print("Type of service:", resource)

print()

# print att
print("Att.:",resource.buckets.all())

print()

#how info of buckets
bucket_list =list(resource.buckets.all())
print("Info about boto3 buckets I have created:")
print(bucket_list)

print()

# this prints every bucket I have in AWS
print("Bucket names in my AWS:")
for i in resource.buckets.all():
    print(i.name)
    
print()

# prints how many buckets I have in my AWS account
print("I have created",len(bucket_list), "buckets in AWS.")