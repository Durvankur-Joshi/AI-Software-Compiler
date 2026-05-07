import json
import re


class JSONRepair:

    def repair(
        self,
        raw_text: str
    ):

        cleaned = raw_text.strip()

        # Remove markdown wrappers
        cleaned = cleaned.replace(
            "```json",
            ""
        )

        cleaned = cleaned.replace(
            "```",
            ""
        )

        # Remove trailing commas
        cleaned = re.sub(
            r",\s*}",
            "}",
            cleaned
        )

        cleaned = re.sub(
            r",\s*]",
            "]",
            cleaned
        )

        # Extract JSON object only
        start = cleaned.find("{")
        end = cleaned.rfind("}")

        if start != -1 and end != -1:

            cleaned = cleaned[
                start:end + 1
            ]

        return json.loads(cleaned)