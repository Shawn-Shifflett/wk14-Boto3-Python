# get all EC2

import boto3

ec2Resource = boto3.client("ec2")

allEC2 = ec2Resource.describe_instances()

# below will print all info about all
#print(allEC2)

print()

allEC2.keys()

print("Number of EC2s:",len(allEC2["Reservations"]))

print()

#additional metadata info
print(allEC2["ResponseMetadata"])