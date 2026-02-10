import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # AWS
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

    # Groq AI
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
