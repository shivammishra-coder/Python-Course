import requests
import time
import logging

class BaseLLMClient:
    def __init__(self, base_url, api_key, model_name, max_retries=3):
        self.base_url = base_url
        self.api_key = api_key
        self.model_name = model_name
        self.max_retries = max_retries

    def call(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "temperature": 0.3
        }

        for attempt in range(self.max_retries):
            try:
                response = requests.post(self.base_url, json=payload, headers=headers, timeout=30)
                response.raise_for_status()
                return response.json()["output"]
            except Exception as e:
                logging.error(f"API error (attempt {attempt+1}): {e}")
                time.sleep(2 ** attempt)

        raise RuntimeError("Max retries exceeded for LLM API")
        

class ModelAClient(BaseLLMClient):
    pass

class ModelBClient(BaseLLMClient):
    pass