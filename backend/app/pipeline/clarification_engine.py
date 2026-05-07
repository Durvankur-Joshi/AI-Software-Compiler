class ClarificationEngine:

    def analyze(
        self,
        user_prompt: str
    ):

        prompt = user_prompt.lower()

        questions = []

        clarification_needed = False

        # Very short prompts
        if len(prompt.split()) < 4:

            clarification_needed = True

            questions.append(
                "What type of application do you want to build?"
            )

        # Missing core business domain
        keywords = [
            "crm",
            "ecommerce",
            "dashboard",
            "hospital",
            "school",
            "chat",
            "social",
            "booking",
            "management",
            "analytics"
        ]

        has_domain = any(
            keyword in prompt
            for keyword in keywords
        )

        if not has_domain:

            clarification_needed = True

            questions.append(
                "What business domain should the application target?"
            )

        # Missing auth expectations
        auth_keywords = [
            "login",
            "auth",
            "authentication",
            "roles",
            "admin"
        ]

        has_auth = any(
            keyword in prompt
            for keyword in auth_keywords
        )

        if not has_auth:

            questions.append(
                "Should the application include authentication and role-based access?"
            )

        return {

            "clarification_needed": clarification_needed,

            "questions": questions
        }