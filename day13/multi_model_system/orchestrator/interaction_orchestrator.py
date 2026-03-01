from clients.llama_client import LlamaClient
from clients.deepseek_client import DeepSeekClient
from prompts.prompt_builder import PromptBuilder
from utils.validator import validate_relevance

class InteractionOrchestrator:

    def __init__(self):
        self.model_a = LlamaClient()
        self.model_b = DeepSeekClient()

    def run(self, topic: str):

        # Turn 1: A
        a1 = self.model_a.call_model(PromptBuilder.initial(topic))
        if not validate_relevance(topic, a1):
            raise Exception("Model A initial response not relevant.")

        # Turn 2: B
        b1 = self.model_b.call_model(PromptBuilder.critique(topic, a1))
        if not validate_relevance(topic, b1):
            raise Exception("Model B critique not relevant.")

        # Turn 3: A
        a2 = self.model_a.call_model(PromptBuilder.final_reply(topic, b1))
        if not validate_relevance(topic, a2):
            raise Exception("Model A final reply not relevant.")

        # Conclusion
        conclusion = self.model_b.call_model(
            PromptBuilder.conclusion(topic, a1, b1, a2)
        )

        return {
            "topic": topic,
            "model_a_initial_response": a1,
            "model_b_critique": b1,
            "model_a_final_reply": a2,
            "synthesized_conclusion": conclusion
        }