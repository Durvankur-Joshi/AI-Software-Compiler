from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    GEMINI_API_KEY: str
    MODEL_NAME: str

    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()