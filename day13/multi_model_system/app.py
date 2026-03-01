import json
from config import validate_config
from orchestrator.interaction_orchestrator import InteractionOrchestrator

def main():
    try:
        validate_config()
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return

    topic = input("Enter discussion topic: ").strip()

    if not topic:
        print(json.dumps({"error": "Topic cannot be empty."}))
        return

    orchestrator = InteractionOrchestrator()

    try:
        result = orchestrator.run(topic)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()