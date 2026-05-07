class SchemaValidator:

    def validate(
        self,
        database_schema,
        api_schema,
        ui_schema,
        auth_schema
    ):

        errors = []

        errors.extend(
            self.validate_database(
                database_schema
            )
        )

        errors.extend(
            self.validate_api_vs_db(
                database_schema,
                api_schema
            )
        )

        errors.extend(
            self.validate_auth_vs_api(
                api_schema,
                auth_schema
            )
        )

        errors.extend(
            self.validate_ui_vs_api(
                ui_schema,
                api_schema
            )
        )

        return errors

    def validate_database(
        self,
        database_schema
    ):

        errors = []

        for table in database_schema.get("tables", []):

            column_names = [
                column["name"]
                for column in table.get("columns", [])
            ]

            if "id" not in column_names:

                errors.append(
                    f'{table["table_name"]} missing id field'
                )

        return errors

    def validate_api_vs_db(
        self,
        database_schema,
        api_schema
    ):

        errors = []

        db_fields = set()

        for table in database_schema.get("tables", []):

            for column in table.get("columns", []):

                db_fields.add(
                    column["name"]
                )

        for endpoint in api_schema.get("endpoints", []):

            for field in endpoint.get(
                "request_fields",
                []
            ):

                if (
                    field not in db_fields
                    and field != "password"
                ):

                    errors.append(
                        f"API request field '{field}' not found in DB schema"
                    )

            for field in endpoint.get(
                "response_fields",
                []
            ):

                if (
                    field not in db_fields
                    and field not in [
                        "token",
                        "message",
                        "data"
                    ]
                ):

                    errors.append(
                        f"API response field '{field}' not found in DB schema"
                    )

        return errors

    def validate_auth_vs_api(
        self,
        api_schema,
        auth_schema
    ):

        errors = []

        api_routes = set()

        for endpoint in api_schema.get("endpoints", []):

            api_routes.add(
                endpoint["path"]
            )

        for permission in auth_schema.get(
            "permissions",
            []
        ):

            for route in permission.get(
                "allowed_routes",
                []
            ):

                if route not in api_routes:

                    errors.append(
                        f"Auth route '{route}' does not exist in API schema"
                    )

        return errors

    def validate_ui_vs_api(
        self,
        ui_schema,
        api_schema
    ):

        errors = []

        api_routes = [
            endpoint["path"]
            for endpoint in api_schema.get("endpoints", [])
        ]

        has_contacts_api = any(
            "/contacts" in route
            for route in api_routes
        )

        for page in ui_schema.get("pages", []):

            page_name = page.get("name", "")

            if (
                "Contact" in page_name
                and not has_contacts_api
            ):

                errors.append(
                    "UI references contacts but contacts API missing"
                )

        return errors