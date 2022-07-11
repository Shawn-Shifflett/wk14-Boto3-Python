# scan table 
import boto3

def scanTable():
    dbTABLE = boto3.resource("dynamodb")
    
    tableName = dbTABLE.Table('musicians')
    
    tableScan = tableName.scan()
    tableScan['Items']
    
    print(tableScan)
    
    
print("Items in table:")
print(scanTable())
