import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd

dynamodb_client = boto3.client('dynamodb','us-west-2')

class DDB:
    def __init__(self, table_name,region):
        try:
            self.dynamodb = boto3.resource('dynamodb', region_name=region)  
            self.table = self.dynamodb.Table(table_name)
        except NoCredentialsError:
            print("AWS credentials not found. Please configure your AWS credentials.")
            exit(1)

    
    def create_table(self,table_name):
        table = self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'ID',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'prompt',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'ID',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'prompt',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def query_table(self):
        response = self.table.scan()
        items = response.get('Items', [])
        return items

    def items_to_dataframe(self, items):
        df = pd.DataFrame(items)
        return df

    def update_table_from_dataframe(self, df):
        for _, row in df.iterrows():
            item = {
                'Attribute1': str(row['Attribute1']),
                'Attribute2': str(row['Attribute2'])
            }
            self.table.put_item(Item=item)
            
    def add_item_to_table(self, ID, category, prompt):
        item = {
            'ID': str(ID),
            'prompt': str(prompt),
            'category': str(category)
        }
        self.table.put_item(Item=item)
        print(f"Item added to the table: {item}")
        
    def table_exists(self, table_name):
        existing_tables = dynamodb_client.list_tables()['TableNames']
        if table_name not in existing_tables:
            return False
        else:
            return True
