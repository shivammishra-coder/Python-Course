import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = os.getenv("BASE_API_URL")
VERIFY_SSL = os.getenv("VERIFY_SSL", "False").lower() == "true"

MODEL_A_NAME = os.getenv("MODEL_A_NAME")
MODEL_B_NAME = os.getenv("MODEL_B_NAME")

MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 120))

LOG_FILE_PATH = "logs/multi_model_system.log"

def validate_config():
    if not BASE_API_URL or not MODEL_A_NAME or not MODEL_B_NAME:
        raise ValueError("Missing required configuration in .env file.")