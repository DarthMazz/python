import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')

for tbl in dynamodb.tables.all():
    print(tbl.name)
    table = dynamodb.Table(tbl.name)
    table.put_item(Item={'jobid': '001', 'Title': 'Title-1'})
    item = table.get_item(Key={'jobid': '001'})['Item']
    print(item)
    item['Title'] = 'hogehoge'
    item['Status'] = 'atari'
    table.put_item(Item=item)