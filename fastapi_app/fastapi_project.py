import os
import sys
from fastapi_app.logger import logger


def create_project_dir(project_name, args) -> None:
    # Define directories
    project_dir = os.path.join(project_name)

    if os.path.exists(project_dir) and not "--force" in args:
        logger.warning(
            f"Project directory {project_dir} already exists, this will overwrite the existing files crated with create_project only, use --force to overwrite"
        )
        sys.exit(1)

    logger.info("Creating FastAPI project structure")

    os.makedirs(project_dir, exist_ok=True)
    logger.info(f"Created directory: {project_dir}")


def create_project_structure(args) -> None:

    project_name = args[0]

    optional_files = [".gitignore", "Dockerfile", "config.py"]

    create_project_dir(project_name=project_name, args=args)

    # Create project files with content
    content = {
        os.path.join(project_name, "main.py"): open(
            "fastapi_app/static/main.py"
        ).read(),
        os.path.join(
            project_name, "README.md"
        ): f"# {project_name}\n\n### This is a FastAPI project created with fastapi-app\n\n### Find the documentation at [Fastapi_app](https://github.com/BimalSteinn/fastapi_app)",
        os.path.join(project_name, "requirements.txt"): "fastapi\nuvicorn\npydantic",
    }

    for file in optional_files:
        if file in args:
            content[os.path.join(project_name, file)] = open(
                f"fastapi_app/static/{file}"
            ).read()

    for file, text in content.items():
        with open(file, "w") as f:
            f.write(text)
        logger.info(f"Created file: {file}")
