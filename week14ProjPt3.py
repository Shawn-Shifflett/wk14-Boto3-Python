# add to table

import boto3

def addToDYDBtable():
    
    # connect to table to add
    dbTABLE = boto3.resource("dynamodb", region_name='us-east-1')
    
    # click on table you want 
    tableName = dbTABLE.Table('musicians')
    
    # add to table
    with tableName.batch_writer() as batch:
        batch.put_item(Item = {'Name' : 'Alison Wonderland', 'Genre' : 'House/Bass'},) #1
        batch.put_item(Item = {'Name' : 'Excision', 'Genre' : 'Bass'},) #2
        batch.put_item(Item = {'Name' : 'Kanye', 'Genre' : 'Rap'},) #3
        batch.put_item(Item = {'Name' : 'Future', 'Genre' : 'Rap'},) #4 
        batch.put_item(Item = {'Name' : 'Chris Luno', 'Genre' : 'House'},) #5
        batch.put_item(Item = {'Name' : 'Slander', 'Genre' : 'House/Bass'},) #6
        batch.put_item(Item = {'Name' : 'G Herbo', 'Genre' : 'Rap'},) #7
        batch.put_item(Item = {'Name' : 'LUCII', 'Genre' : 'House/Bass'},) #8
        batch.put_item(Item = {'Name' : 'Rufus Du Sol', 'Genre' : 'House'},) #9
        batch.put_item(Item = {'Name' : 'Meek Mill', 'Genre' : 'Rap'},) #10
    print(batch)
print(addToDYDBtable())