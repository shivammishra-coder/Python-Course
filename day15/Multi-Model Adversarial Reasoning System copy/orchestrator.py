import logging
from typing import Optional

from api_clients import ModelAClient, ModelBClient
from prompt_builder import PromptBuilder
from validator import validate_topic, validate_final_json
from logger import log_prompt, log_response
from formatter import OutputFormatter


class AdversarialOrchestrator:

    def __init__(
        self,
        model_a_client: ModelAClient,
        model_b_client: ModelBClient
    ):
        self.model_a = model_a_client
        self.model_b = model_b_client

    def run(self, user_input: str) -> str:
        try:
            # validate input
            validate_topic(user_input)

            # Model A - initial
            prompt_a1 = PromptBuilder.build_model_a_initial(user_input)
            log_prompt("ModelA-Turn1", prompt_a1)

            raw_a_initial = self.model_a.call(prompt_a1)
            log_response("ModelA-Turn1", raw_a_initial)

            a_initial = OutputFormatter.normalize_model_a_initial(raw_a_initial)

            # Model B - critique
            prompt_b = PromptBuilder.build_model_b_critique(
                user_input,
                a_initial
            )
            log_prompt("ModelB", prompt_b)

            raw_b_critique = self.model_b.call(prompt_b)
            log_response("ModelB", raw_b_critique)

            b_critique = OutputFormatter.normalize_model_b_critique(raw_b_critique)

            # Model A - revision
            prompt_a2 = PromptBuilder.build_model_a_revision(
                user_input,
                a_initial,
                b_critique
            )
            log_prompt("ModelA-Turn2", prompt_a2)

            raw_a_revised = self.model_a.call(prompt_a2)
            log_response("ModelA-Turn2", raw_a_revised)

            a_revised = OutputFormatter.normalize_model_a_revised(raw_a_revised)

            # evaluate robustness
            final_evaluation = self.evaluate(
                a_initial,
                b_critique,
                a_revised
            )

            # build final json
            formatted_output = OutputFormatter.build_final_json(
                original_input=user_input,
                model_a_initial=a_initial,
                model_b_critique=b_critique,
                model_a_revised=a_revised,
                final_evaluation=final_evaluation
            )

            validate_final_json(formatted_output)

            return OutputFormatter.to_strict_json(formatted_output)

        except Exception as e:
            logging.exception("Adversarial orchestration failed.")
            raise RuntimeError(f"Adversarial system failed: {str(e)}")

    def evaluate(
        self,
        a_initial: str,
        b_critique: str,
        a_revised: str
    ) -> str:

        improvement_detected = (
            "REBUTTALS:" in a_revised and
            "UPDATED_RISKS:" in a_revised
        )

        if improvement_detected and len(a_revised) > len(a_initial):
            return (
                "Model A incorporated critique and improved risk analysis. "
                "Residual risks may remain."
            )

        if improvement_detected:
            return (
                "Model A responded to critique but improvement depth may be limited."
            )

        return (
            "Revision shows limited structural response. Robustness uncertain."
        )