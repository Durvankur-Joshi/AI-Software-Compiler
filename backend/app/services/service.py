import time
from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


class GeminiService:

    def generate_json(
        self,
        prompt: str,
        retries: int = 5
    ):

        attempt = 0

        while attempt < retries:

            try:

                response = client.chat.completions.create(
                    model="poolside/laguna-xs.2:free",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a strict software compiler system. "
                                "Always return valid JSON only."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0
                )

                return response.choices[0].message.content

            except Exception as e:

                print(f"\nRetry Attempt {attempt + 1} Failed:")
                print(str(e))

                attempt += 1

                if attempt >= retries:
                    raise Exception(
                        f"LLM failed after {retries} retries"
                    )

                wait_time = 5 * attempt

                print(f"\nRetrying in {wait_time} seconds...\n")

                time.sleep(wait_time)


gemini_service = GeminiService()