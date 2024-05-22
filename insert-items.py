import boto3

def insert_item(table_name, item):
    dynamodb = boto3.client('dynamodb')
    try:
        # Insert item into DynamoDB table
        dynamodb.put_item(
            TableName=table_name,
            Item=item
        )
        print("Item inserted successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    item = {
        'name': {'S': 'Siddhesh'},
        'cgpa': {'N': '8.9'},
        'age': {'N': '22'}
    }
    insert_item(table_name, item)
