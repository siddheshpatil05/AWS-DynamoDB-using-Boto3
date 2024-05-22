import boto3

def update_item(table_name, key, update_expression, expression_attribute_values):
    dynamodb = boto3.client('dynamodb')
    try:
        # Update item in DynamoDB table
        dynamodb.update_item(
            TableName=table_name,
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        print("Item updated successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    table_name = 'try-siddhesh'  # Replace with your table name
    key = {'name': {'S': 'Siddhesh'}}  # Replace with your primary key
    update_expression = "SET cgpa = :cgpa, age = :age"
    expression_attribute_values = {
        ':cgpa': {'N': '9.0'},
        ':age': {'N': '24'}
    }
    update_item(table_name, key, update_expression, expression_attribute_values)
