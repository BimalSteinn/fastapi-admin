import os
import sys

from fastapi_app.logger import logger


def create_app_structure(args):

    app_name = args[0]
    # Define directories and files
    dirs = [app_name]

    # Check if the directory already exists with the same name
    if os.path.exists(app_name) and not "--force" in args:
        logger.warning(
            f"App directory {app_name} already exists, this will overwrite the existing files crated with create_app only, use --force to overwrite"
        )
        sys.exit(1)

    files = [
        os.path.join(app_name, "models.py"),
        os.path.join(app_name, "schemas.py"),
        os.path.join(app_name, "__init__.py"),
        os.path.join(app_name, "handler.py"),
    ]

    contents = [
        "# Place your ORM models here",
        "# Place your Pydantic models here",
        "",
        "from fastapi import APIRouter\n\nrouter = APIRouter()",
    ]

    # Create directories
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        logger.info(f"Created directory: {dir}")

    # Create files with content
    for file, content in zip(files, contents):
        with open(file, "w") as f:
            f.write(content)
        logger.info(f"Created file: {file}")
