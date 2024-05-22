import boto3

def delete_table(table_name):
    dynamodb = boto3.client('dynamodb')
    try:
        # Delete DynamoDB table
        dynamodb.delete_table(TableName=table_name)
        print(f"DynamoDB table '{table_name}' deleted.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    delete_table(table_name)
