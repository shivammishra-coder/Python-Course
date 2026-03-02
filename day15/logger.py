import logging
from datetime import datetime

logging.basicConfig(
    filename="adversarial_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_prompt(model_name, prompt):
    logging.info(f"[PROMPT - {model_name}]\n{prompt}")

def log_response(model_name, response):
    logging.info(f"[RESPONSE - {model_name}]\n{response}")