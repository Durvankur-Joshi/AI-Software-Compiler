import os


class ExecutionValidator:

    def validate(self, project_id):

        errors = []

        base_path = f"generated/{project_id}/backend"

        required_files = [

            f"{base_path}/main.py",

            f"{base_path}/database.py",
        ]

        required_directories = [

            f"{base_path}/routes",

            f"{base_path}/models",
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

        routes_path = f"{base_path}/routes"

        models_path = f"{base_path}/models"

        route_files = (
            os.listdir(routes_path)
            if os.path.exists(routes_path)
            else []
        )

        model_files = (
            os.listdir(models_path)
            if os.path.exists(models_path)
            else []
        )

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