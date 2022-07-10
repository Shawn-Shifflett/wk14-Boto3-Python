# create multiple EC2s together

import boto3

ec2Resource = boto3.resource("ec2")



multi = ec2Resource.create_instances(
    ImageId = 'ami-0cff7528ff583bf9a', 
    InstanceType = 't2.micro',
    MaxCount = 3,
    MinCount = 3
    )
    
print(multi)