class RepairEngine:

    def repair_api_schema(
        self,
        api_schema,
        db_schema
    ):

        valid_fields = set()

        for table in db_schema.tables:
            for column in table.columns:
                valid_fields.add(column.name)

        for endpoint in api_schema.endpoints:

            endpoint.request_fields = [
                field
                for field in endpoint.request_fields
                if field in valid_fields
            ]

        return api_schema