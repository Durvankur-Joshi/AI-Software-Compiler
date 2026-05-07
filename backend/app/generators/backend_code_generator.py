import os


class BackendCodeGenerator:

    def generate(
        self,
        db_schema,
        api_schema
    ):

        os.makedirs(
            "generated/backend/routes",
            exist_ok=True
        )

        os.makedirs(
            "generated/backend/models",
            exist_ok=True
        )

        self.generate_main_file()

        self.generate_database_file()

        self.generate_models(
            db_schema
        )

        self.generate_routes(
            api_schema
        )

    def generate_main_file(self):

        content = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Generated Backend Running"}
"""

        with open(
            "generated/backend/main.py",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

    def generate_database_file(self):

        content = """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///generated_app.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
"""

        with open(
            "generated/backend/database.py",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

    def generate_models(
        self,
        db_schema
    ):

        for table in db_schema.get(
            "tables",
            []
        ):

            model_name = table["table_name"]

            fields = []

            for column in table.get(
                "columns",
                []
            ):

                if column["name"] == "id":
                    continue

                fields.append(
                    f'    {column["name"]}: str'
                )

            content = f"""
from pydantic import BaseModel


class {model_name.capitalize()}Model(BaseModel):

{chr(10).join(fields)}
"""

            with open(
                f"generated/backend/models/{model_name}.py",
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)

    def generate_routes(
        self,
        api_schema
    ):

        grouped_routes = {}

        for endpoint in api_schema.get(
            "endpoints",
            []
        ):

            path = endpoint["path"]

            resource = (
                path.split("/")[1]
                if len(path.split("/")) > 1
                else "root"
            )

            if resource not in grouped_routes:

                grouped_routes[resource] = []

            grouped_routes[resource].append(
                endpoint
            )

        for resource, endpoints in grouped_routes.items():

            lines = []

            lines.append(
                "from fastapi import APIRouter"
            )

            lines.append("")
            lines.append(
                "router = APIRouter()"
            )
            lines.append("")

            for endpoint in endpoints:

                method = endpoint[
                    "method"
                ].lower()

                path = endpoint["path"]

                lines.append(
                    f'@router.{method}("{path}")'
                )

                lines.append(
                    f"def {method}_{resource}():"
                )

                lines.append(
                    '    return {"message": "Generated endpoint"}'
                )

                lines.append("")

            content = "\n".join(lines)

            with open(
                f"generated/backend/routes/{resource}.py",
                "w",
                encoding="utf-8"
            ) as file:

                file.write(content)