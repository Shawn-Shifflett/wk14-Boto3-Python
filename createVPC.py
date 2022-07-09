# create Virtual Private Cloud (VPC) using python

import boto3

ec2CLIENT = boto3.client("ec2")
vpc = ec2CLIENT.create_vpc(CidrBlock = '10.0.0.0/16')

print(vpc) 