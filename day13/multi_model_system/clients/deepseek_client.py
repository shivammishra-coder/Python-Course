from clients.base_client import BaseChatClient
from config import MODEL_B_NAME

class DeepSeekClient(BaseChatClient):
    def __init__(self):
        super().__init__(MODEL_B_NAME)