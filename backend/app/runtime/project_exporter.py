import shutil


class ProjectExporter:

    def export_backend(self, project_id):

        output_zip = f"generated/{project_id}"

        generated_path = (
            f"generated/{project_id}/backend"
        )

        zip_path = shutil.make_archive(
            output_zip,
            "zip",
            generated_path
        )

        return zip_path