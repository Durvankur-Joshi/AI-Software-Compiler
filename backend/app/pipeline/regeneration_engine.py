from app.services.gemini_service import gemini_service

import json


class RegenerationEngine:

    def regenerate_api_schema(
        self,
        user_prompt,
        database_schema,
        validation_errors
    ):

        prompt = f"""
You are an API schema repair engine.

The original user request was:

{user_prompt}

Database Schema:

{json.dumps(database_schema, indent=2)}

Validation Errors:

{json.dumps(validation_errors, indent=2)}

Generate ONLY corrected API schema.

Return STRICT JSON ONLY.

Required Format:

{{
  "endpoints": [
    {{
      "path": "string",
      "method": "GET",
      "request_fields": [],
      "response_fields": []
    }}
  ]
}}
"""

        response = gemini_service.generate(prompt)

        cleaned = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned)