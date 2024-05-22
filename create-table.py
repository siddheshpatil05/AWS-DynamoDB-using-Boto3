import boto3

def create_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        # Create DynamoDB table
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"DynamoDB table '{table_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    create_table(table_name)
