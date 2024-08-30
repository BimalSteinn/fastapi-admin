# fastapi_app

A command-line tool to create a FastAPI app with a predefined directory structure and files.

## Installation

You can install this package from PyPI:

```bash
pip install fastapi_app
```

## Usage

### User the command to create empty project

```bash
fastapi_app create_project <project_name>
```

There is one optional argument
- --force - Overwrite the project directory if it already exists

### Go to that project
```bash
cd <project_name>
```

### Use the command to create a new FastAPI app
```bash
fastapi_app create_app <app_name>
```
This will generate a FastAPI app.
