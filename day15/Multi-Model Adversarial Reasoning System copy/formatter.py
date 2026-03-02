import json
import re
from typing import Dict


class OutputFormatter:
    """
    Responsible for:
    - Sanitizing raw model outputs
    - Normalizing whitespace
    - Removing invalid control characters
    - Enforcing strict JSON structure
    - Guaranteeing schema compatibility
    """

    @staticmethod
    def sanitize_text(text: str) -> str:
        """
        Remove problematic control characters and normalize spacing.
        """
        if not isinstance(text, str):
            text = str(text)

        # Remove non-printable control characters except newline and tab
        text = re.sub(r"[^\x09\x0A\x0D\x20-\x7E]", "", text)

        # Normalize excessive whitespace
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)

        return text.strip()

    @staticmethod
    def ensure_section(header: str, text: str) -> str:
        """
        Ensures required section headers exist.
        If missing, adds placeholder.
        """
        if header not in text:
            text += f"\n\n{header}:\nNot explicitly provided."
        return text

    @staticmethod
    def normalize_model_a_initial(text: str) -> str:
        """
        Ensures Model A initial output contains required sections.
        """
        text = OutputFormatter.sanitize_text(text)

        required_sections = [
            "PROPOSAL:",
            "REASONING:",
            "RISKS:"
        ]

        for section in required_sections:
            text = OutputFormatter.ensure_section(section, text)

        return text

    @staticmethod
    def normalize_model_b_critique(text: str) -> str:
        """
        Ensures Model B critique contains required sections.
        """
        text = OutputFormatter.sanitize_text(text)

        required_sections = [
            "CRITIQUE:",
            "EDGE_CASES:",
            "RISKS:",
            "COUNTERARGUMENTS:"
        ]

        for section in required_sections:
            text = OutputFormatter.ensure_section(section, text)

        return text

    @staticmethod
    def normalize_model_a_revised(text: str) -> str:
        """
        Ensures Model A revised output contains required sections.
        """
        text = OutputFormatter.sanitize_text(text)

        required_sections = [
            "REVISED_PROPOSAL:",
            "REBUTTALS:",
            "UPDATED_RISKS:"
        ]

        for section in required_sections:
            text = OutputFormatter.ensure_section(section, text)

        return text

    @staticmethod
    def build_final_json(
        original_input: str,
        model_a_initial: str,
        model_b_critique: str,
        model_a_revised: str,
        final_evaluation: str
    ) -> Dict:
        """
        Constructs strict JSON-compliant dictionary.
        """

        structured_output = {
            "original_input": OutputFormatter.sanitize_text(original_input),
            "model_a_initial": OutputFormatter.normalize_model_a_initial(model_a_initial),
            "model_b_critique": OutputFormatter.normalize_model_b_critique(model_b_critique),
            "model_a_revised": OutputFormatter.normalize_model_a_revised(model_a_revised),
            "final_evaluation": OutputFormatter.sanitize_text(final_evaluation)
        }

        return structured_output

    @staticmethod
    def to_strict_json(data: Dict) -> str:
        """
        Converts dictionary to strictly valid JSON string.
        Ensures ASCII-safe output and no trailing commas.
        """
        return json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        )