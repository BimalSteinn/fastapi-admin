import sys
from fastapi_app.fastapi_app import create_app_structure
from fastapi_app.fastapi_project import create_project_structure
from fastapi_app.help import fastapi_app_help

from fastapi_app.logger import logger

FUNCTION_MAP = {
    "create_app": {"name": create_app_structure, "min_args": 1, "max_args": 1},
    "create_project": {"name": create_project_structure, "min_args": 1, "max_args": 5},
    "--help": {"name": fastapi_app_help, "min_args": 0, "max_args": 0},
}


def main():
    if len(sys.argv) < 2:
        fastapi_app_help([])
        sys.exit(1)

    command = sys.argv[1]

    arguments = sys.argv[2:]

    if command not in FUNCTION_MAP:
        logger.info(f"Invalid command: {command} type fastapi_app --help for help")
        sys.exit(1)

    if (
        len(arguments) < FUNCTION_MAP[command]["min_args"]
        or len(arguments) > FUNCTION_MAP[command]["max_args"]
    ):
        logger.info(
            f"Invalid number of arguments for {command}, Use fastapi_app --help for help"
        )
        sys.exit(1)

    FUNCTION_MAP[command]["name"](arguments)


if __name__ == "__main__":
    main()
