import sqlite3
import os


class SQLiteRuntime:

    def create_database(self, db_schema):

        os.makedirs(
            "generated",
            exist_ok=True
        )

        connection = sqlite3.connect(
            "generated/generated_app.db"
        )

        cursor = connection.cursor()

        for table in db_schema["tables"]:

            columns = []

            for column in table["columns"]:

                # Prevent duplicate id column
                if column["name"].lower() == "id":
                    continue

                sql_type = column["type"].upper()

                if sql_type not in [
                    "TEXT",
                    "INTEGER",
                    "BOOLEAN"
                ]:
                    sql_type = "TEXT"

                columns.append(
                    f'{column["name"]} {sql_type}'
                )

            query = f"""
            CREATE TABLE IF NOT EXISTS
            {table["table_name"]}
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {",".join(columns)}
            )
            """

            print("\nSQL QUERY:\n")
            print(query)

            cursor.execute(query)

        connection.commit()

        connection.close()