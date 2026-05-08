import json

from app.services.gemini_service import gemini_service
from app.pipeline.json_repair import JSONRepair


class CompilerAgent:

    def __init__(self):

        self.json_repair = JSONRepair()

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
  }},

  "business_logic": {{
    "role_rules": ["string"],
    "premium_features": ["string"],
    "restrictions": ["string"]
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
9. Include business logic rules.
10. Include role-based restrictions.
11. Include premium feature gating if applicable.
12. Restrictions must be human-readable strings.
"""

        response = gemini_service.generate_json(prompt)

        result = self.json_repair.repair(
            response
        )

        return result