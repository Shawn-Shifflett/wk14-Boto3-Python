import boto3

client = boto3.client("ec2")

delVPC = client.delete_vpc(
    VpcId = "vpc-0aebfdb4e67509853"
    )
    
print(delVPC)