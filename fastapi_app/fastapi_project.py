import os


def create_project_structure(args) -> None:

    project_name = args[0]

    # Define directories
    project_dir = os.path.join(project_name)

    if os.path.exists(project_dir) and not "--force" in args:
        print(
            f"Project directory {project_dir} already exists, this will overwrite the existing files crated with createproject only, use --force to overwrite"
        )
        return

    print("Creating FastAPI project structure")

    os.makedirs(project_dir, exist_ok=True)
    print(f"Created directory: {project_dir}")

    # Create project files with content
    content = {
        os.path.join(project_name, "main.py"): (
            "from fastapi import FastAPI\n\n"
            "app = FastAPI()\n\n"
            '@app.get("/")\n'
            "def read_root():\n"
            '    return {"message": "Hello World!"}'
        ),
        os.path.join(
            project_name, "README.md"
        ): f"# {project_name}\n\n### This is a FastAPI project created with fastapi-app\n\n### Find the documentation at [Fastapi_app](https://github.com/BimalSteinn/fastapi_app)",
        os.path.join(project_name, "requirements.txt"): "fastapi\nuvicorn",
    }

    for file, text in content.items():
        with open(file, "w") as f:
            f.write(text)
        print(f"Created file: {file}")
