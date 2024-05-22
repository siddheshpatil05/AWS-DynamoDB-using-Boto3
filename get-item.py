import boto3

def get_item(table_name, key):
    dynamodb = boto3.client('dynamodb')
    try:
        # Retrieve item from DynamoDB table
        response = dynamodb.get_item(
            TableName=table_name,
            Key=key
        )
        item = response.get('Item', {})
        print("Retrieved item:", item)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    key = {'name': {'S': 'Siddhesh'}}  # Replace with your primary key
    get_item(table_name, key)
