import boto3
from botocore.exceptions import ClientError

AWS_REGION = "us-east-1"
TABLE_NAME = "users"

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
users_table = dynamodb.Table(TABLE_NAME)

def create_user(name, email, password):
    try:
        users_table.put_item(
            Item={
                "email": email,
                "name": name,
                "password": password
            },
            ConditionExpression="attribute_not_exists(email)"
        )
        return True
    except ClientError:
        return False

def authenticate_user(email, password):
    try:
        response = users_table.get_item(Key={"email": email})
        user = response.get("Item")

        if user and user["password"] == password:
            return {
                "name": user["name"],
                "email": user["email"]
            }
        return None
    except ClientError:
        return None
