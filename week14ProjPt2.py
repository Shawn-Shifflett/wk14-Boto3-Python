# connection

import boto3

# replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='shifflettko@battlers.ab.edu',
    aws_secret_access_key='Kos11211997!',
    )
print("Connection Success")