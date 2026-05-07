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
            "name": "id",
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
    ]
  }},

  "auth": {{
    "roles": ["string"],
    "permissions": []
  }}
}}

Rules:

1. Every database table MUST contain id field.
2. Use TEXT datatype for SQLite.
3. Create CRUD APIs.
4. Include login/register APIs.
5. Include admin permissions if admin exists.
6. Return VALID JSON ONLY.
7. No markdown.
8. No explanation.
"""

        response = gemini_service.generate_json(prompt)

        cleaned = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        result = json.loads(cleaned)

        # Inject fake invalid field for testing
        result["api"]["endpoints"][0]["request_fields"].append(
            "fake_field_xyz"
        )

        return result