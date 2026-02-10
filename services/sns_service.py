import boto3

AWS_REGION = "us-east-1"

# 🔴 PASTE YOUR ACTUAL ARN BELOW
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:123456789012:aws_capstone_topic"

sns_client = boto3.client("sns", region_name=AWS_REGION)

def send_notification(subject, message):
    """
    Send notification using AWS SNS
    """
    try:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )
    except Exception as e:
        print("SNS Error:", e)
