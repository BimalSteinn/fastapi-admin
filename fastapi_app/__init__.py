import sys
from fastapi_app.fastapi_app import create_app_structure


def main():
    if len(sys.argv) != 2:
        print("Usage: fastapi_app <app_name>")
        sys.exit(1)

    app_name = sys.argv[1]
    create_app_structure(app_name)


if __name__ == "__main__":
    main()
