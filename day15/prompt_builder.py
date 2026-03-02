class PromptBuilder:

    @staticmethod
    def build_model_a_initial(user_input):
        return f"""You are Model A...

PROPOSAL:
...
User Scenario:
{user_input}
"""

    @staticmethod
    def build_model_b_critique(user_input, model_a_output):
        return f"""You are Model B...

Original Scenario:
{user_input}

Model A Proposal:
{model_a_output}
"""

    @staticmethod
    def build_model_a_revision(user_input, model_a_output, model_b_output):
        return f"""You are Model A...

Original Scenario:
{user_input}

Your Original Proposal:
{model_a_output}

Model B Critique:
{model_b_output}
"""