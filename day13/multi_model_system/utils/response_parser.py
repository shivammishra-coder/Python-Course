def extract_chat_content(response_json: dict) -> str:
    try:
        return response_json["message"]["content"]
    except Exception:
        return str(response_json)