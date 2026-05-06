import json

from app.services.gemini_service import gemini_service


class CompilerAgent:

    def run(self, user_prompt: str):

        prompt = f"""
You are an AI software architect.

Generate COMPLETE application blueprint JSON.

User Request:
{user_prompt}

Return STRICT JSON ONLY.

Required JSON Structure:

{{
  "intent": {{
    "app_name": "string",
    "app_type": "string",
    "features": ["string"],
    "user_roles": ["string"]
  }},

  "architecture": {{
    "entities": [
      {{
        "name": "string",
        "fields": ["string"]
      }}
    ],

    "pages": ["string"],

    "modules": ["string"],

    "roles": ["string"]
  }},

  "database": {{
    "tables": [
      {{
        "table_name": "string",
        "columns": [
          {{
            "name": "string",
            "type": "TEXT",
            "required": true
          }}
        ]
      }}
    ]
  }},

  "api": {{
    "endpoints": [
      {{
        "path": "string",
        "method": "GET",
        "request_fields": [],
        "response_fields": []
      }}
    ]
  }},

  "ui": {{
    "pages": [
      {{
        "name": "string",
        "components": []
      }}
        return json.loads(response)