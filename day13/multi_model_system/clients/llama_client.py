from clients.base_client import BaseChatClient
from config import MODEL_A_NAME

class LlamaClient(BaseChatClient):
    def __init__(self):
        super().__init__(MODEL_A_NAME)