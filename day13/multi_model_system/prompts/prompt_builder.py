class PromptBuilder:

    @staticmethod
    def initial(topic):
        return f"""
Topic: {topic}

Provide your clear position, explanation, or argument.
Structure your response with headings if appropriate.
"""

    @staticmethod
    def critique(topic, a_response):
        return f"""
Topic: {topic}

Model A Position:
{a_response}

Critique, question, or expand upon Model A's response.
Be analytical.
"""

    @staticmethod
    def final_reply(topic, b_response):
        return f"""
Topic: {topic}

Model B Critique:
{b_response}

Respond to the critique and refine or defend your position.
"""

    @staticmethod
    def conclusion(topic, a1, b1, a2):
        return f"""
Topic: {topic}

Discussion Summary:
Model A Initial: {a1}
Model B Critique: {b1}
Model A Final: {a2}

Provide a short synthesized conclusion (4-6 sentences).
"""