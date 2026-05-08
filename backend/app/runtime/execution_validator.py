import os


class ExecutionValidator:

    def validate(self):

        errors = []

        required_files = [

            "generated/backend/main.py",

            "generated/backend/database.py",
        ]

        required_directories = [

            "generated/backend/routes",

            "generated/backend/models",
        ]

        for file_path in required_files:

            if not os.path.exists(file_path):

                errors.append(
                    f"Missing file: {file_path}"
                )

        for directory in required_directories:

            if not os.path.exists(directory):

                errors.append(
                    f"Missing directory: {directory}"
                )

        routes_path = "generated/backend/routes"

        models_path = "generated/backend/models"

        route_files = os.listdir(
            routes_path
        ) if os.path.exists(routes_path) else []

        model_files = os.listdir(
            models_path
        ) if os.path.exists(models_path) else []

        if len(route_files) == 0:

            errors.append(
                "No route files generated"
            )

        if len(model_files) == 0:

            errors.append(
                "No model files generated"
            )

        return {

            "valid": len(errors) == 0,

            "errors": errors,

            "generated_routes": route_files,

            "generated_models": model_files
        }