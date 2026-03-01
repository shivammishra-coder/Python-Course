import requests
import time
from config import MAX_RETRIES, REQUEST_TIMEOUT, BASE_API_URL, VERIFY_SSL
from utils.logger import log_info, log_error
from utils.response_parser import extract_chat_content

class BaseChatClient:

    def __init__(self, model_name):
        self.model_name = model_name
        self.endpoint = f"{BASE_API_URL}/chat"

    def call_model(self, prompt: str) -> str:

        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": "Respond in a structured analytical format."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        for attempt in range(MAX_RETRIES):
            try:
                log_info(f"{self.model_name} PROMPT:\n{prompt}")

                response = requests.post(
                    self.endpoint,
                    json=payload,
                    verify=VERIFY_SSL,
                    timeout=REQUEST_TIMEOUT
                )

                response.raise_for_status()
                data = response.json()

                log_info(f"{self.model_name} RAW OUTPUT:\n{data}")

                return extract_chat_content(data)

            except Exception as e:
                log_error(f"{self.model_name} ERROR attempt {attempt+1}: {e}")
                time.sleep(2)

        raise Exception(f"{self.model_name} failed after retries.")