import os


def create_app_structure(app_name):
    # Define directories and files
    dirs = [app_name]

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
        print(f"Created directory: {dir}")

    # Create files with content
    for file, content in zip(files, contents):
        with open(file, "w") as f:
            f.write(content)
        print(f"Created file: {file}")
