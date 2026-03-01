def validate_relevance(topic: str, response: str) -> bool:
    topic_words = topic.lower().split()
    response_lower = response.lower()
    return any(word in response_lower for word in topic_words)