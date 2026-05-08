import os
import zipfile


class BackendGenerator:

    def generate(self, result, project_id):

        base_path = f"generated/{project_id}/backend"

        routes_path = f"{base_path}/routes"
        models_path = f"{base_path}/models"

        os.makedirs(routes_path, exist_ok=True)
        os.makedirs(models_path, exist_ok=True)

        self.generate_database_file(base_path)

        self.generate_models(
            database_schema=result["database"],
            base_path=base_path
        )

        self.generate_routes(
            api_schema=result["api"],
            base_path=base_path
        )

        self.generate_main_file(
            api_schema=result["api"],
            base_path=base_path
        )

        self.generate_requirements_file(
            base_path=base_path
        )

        self.create_zip(project_id)

    def generate_database_file(self, base_path):

        content = """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./generated_app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
"""

        with open(
            f"{base_path}/database.py",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

    def generate_models(
        self,
        database_schema,
        base_path
    ):

        for table in database_schema.get(
            "tables",
            []
        ):

            class_name = table[
                "table_name"
            ].capitalize()

            columns_code = []

            for column in table.get(
                "columns",
                []
            ):

                column_name = column["name"]

                if column_name == "id":

                    columns_code.append(
                        "    id = Column(Integer, primary_key=True, index=True)"
                    )

                    continue

                sql_type = column["type"]

                sqlalchemy_type = "String"

                if sql_type == "INTEGER":
                    sqlalchemy_type = "Integer"

                elif sql_type == "BOOLEAN":
                    sqlalchemy_type = "Boolean"

                columns_code.append(
                    f"    {column_name} = Column({sqlalchemy_type})"
                )

            model_code = f'''
from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class {class_name}(Base):

    __tablename__ = "{table["table_name"]}"

{chr(10).join(columns_code)}
'''

            with open(
                f'{base_path}/models/{table["table_name"]}.py',
                "w",
                encoding="utf-8"
            ) as file:

                file.write(model_code)

    def generate_routes(
        self,
        api_schema,
        base_path
    ):

        grouped_routes = {}

        for endpoint in api_schema.get(
            "endpoints",
            []
        ):

            path = endpoint["path"]

            route_name = path.split("/")[1]

            if route_name not in grouped_routes:

                grouped_routes[
                    route_name
                ] = []

            grouped_routes[
                route_name
            ].append(endpoint)

        for route_group, endpoints in grouped_routes.items():

            route_code = '''
from fastapi import APIRouter

router = APIRouter()
'''

            for endpoint in endpoints:

                path = endpoint["path"]

                method = endpoint[
                    "method"
                ].lower()

                function_name = (
                    method
                    + "_"
                    + path.replace("/", "_")
                    .replace("{", "")
                    .replace("}", "")
                )

                route_code += f'''

@router.{method}("{path}")
def {function_name}():

    return {{
        "message": "{path} works"
    }}
'''

            with open(
                f"{base_path}/routes/{route_group}.py",
                "w",
                encoding="utf-8"
            ) as file:

                file.write(route_code)

    def generate_main_file(
        self,
        api_schema,
        base_path
    ):

        route_groups = set()

        for endpoint in api_schema.get(
            "endpoints",
            []
        ):

            route_name = endpoint[
                "path"
            ].split("/")[1]

            route_groups.add(
                route_name
            )

        imports = []

        includes = []

        for group in route_groups:

            imports.append(
                f"from routes import {group}"
            )

            includes.append(
                f"app.include_router({group}.router)"
            )

        main_code = f'''
from fastapi import FastAPI

{chr(10).join(imports)}

app = FastAPI()

{chr(10).join(includes)}


@app.get("/")
def root():

    return {{
        "message": "AI Generated Backend Running"
    }}
'''

        with open(
            f"{base_path}/main.py",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(main_code)

    def generate_requirements_file(
        self,
        base_path
    ):

        requirements = """
fastapi
uvicorn
sqlalchemy
"""

        with open(
            f"{base_path}/requirements.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(requirements)

    def create_zip(
        self,
        project_id
    ):

        folder_path = f"generated/{project_id}"

        zip_path = f"generated/{project_id}.zip"

        with zipfile.ZipFile(
            zip_path,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zipf:

            for root, dirs, files in os.walk(folder_path):

                for file in files:

                    file_path = os.path.join(
                        root,
                        file
                    )

                    arcname = os.path.relpath(
                        file_path,
                        folder_path
                    )

                    zipf.write(
                        file_path,
                        arcname
                    )