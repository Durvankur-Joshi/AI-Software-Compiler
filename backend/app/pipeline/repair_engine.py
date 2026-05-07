class RepairEngine:

    def repair_api_schema(
        self,
        api_schema,
        db_schema
    ):

        db_fields = set()

        for table in db_schema.get("tables", []):

            for column in table.get("columns", []):

                db_fields.add(
                    column["name"]
                )

        for endpoint in api_schema.get("endpoints", []):

            fixed_request_fields = []

            for field in endpoint.get(
                "request_fields",
                []
            ):

                if (
                    field in db_fields
                    or field == "password"
                ):

                    fixed_request_fields.append(
                        field
                    )

            endpoint["request_fields"] = (
                fixed_request_fields
            )

            fixed_response_fields = []

            for field in endpoint.get(
                "response_fields",
                []
            ):

                if (
                    field in db_fields
                    or field in [
                        "token",
                        "message",
                        "data"
                    ]
                ):

                    fixed_response_fields.append(
                        field
                    )

            endpoint["response_fields"] = (
                fixed_response_fields
            )

        return api_schema