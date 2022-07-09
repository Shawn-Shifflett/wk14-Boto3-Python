# gives info about VPC(s)

import boto3

client = boto3.client("ec2")

#info about the VPCs
infoVPC = client.describe_vpcs()
print("Info about the VPCs in accoount:")
print(infoVPC)

print()

# how many vpc do we have
numm = client.describe_vpcs()
nVPCs = numm["Vpcs"]
lengthVPC = len(nVPCs)

print("We have",lengthVPC, "VPCs in our account.")

print()

# filter VPCs by VPC id
print("Filter VPC by their ID:")
print("(Grab info for this VPC)")
filterVPC = client.describe_vpcs(VpcIds = ["vpc-0aebfdb4e67509853"])
print(filterVPC)