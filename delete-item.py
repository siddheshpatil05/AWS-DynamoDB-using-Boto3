import boto3

def delete_item(table_name, key):
    dynamodb = boto3.client('dynamodb')
    try:
        # Delete item from DynamoDB table
        dynamodb.delete_item(
            TableName=table_name,
            Key=key
        )
        print("Item deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    key = {'name': {'S': 'Siddhesh'}}  # Replace with your primary key
    delete_item(table_name, key)
