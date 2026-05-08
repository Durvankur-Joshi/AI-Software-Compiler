import shutil
import os


class ProjectExporter:

    def export_backend(self):

        output_zip = "generated_backend"

        generated_path = "generated/backend"

        zip_path = shutil.make_archive(
            output_zip,
            "zip",
            generated_path
        )

        return zip_path