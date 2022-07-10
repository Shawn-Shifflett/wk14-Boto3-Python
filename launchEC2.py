# launch EC2

import boto3

ec2Resource = boto3.resource("ec2")



createEC2 = ec2Resource.create_instances(
    ImageId = 'ami-0cff7528ff583bf9a', 
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1
    )
    
print(createEC2)