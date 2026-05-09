import time
import google.generativeai as genai
from app.core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)


class GeminiService:

    def __init__(self):
        self.model = genai.GenerativeModel(
            settings.MODEL_NAME
        )

    def generate_json(
        self,
        prompt: str,
        retries: int = 5
    ):
        attempt = 0

        while attempt < retries:
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0,
                        "response_mime_type": "application/json"
                    }
                )
                return response.text

            except Exception as e:
                print(f"\nRetry Attempt {attempt + 1} Failed:")
                print(str(e))

                if "429" in str(e):
                    wait_time = 60
                else:
                    wait_time = 5 * (attempt + 1)

                attempt += 1

                if attempt >= retries:
                    raise Exception(
                        f"Gemini failed after {retries} retries"
                    )

                print(f"\nRetrying in {wait_time} seconds...\n")
                time.sleep(wait_time)


gemini_service = GeminiService()