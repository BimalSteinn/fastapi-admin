from setuptools import setup, find_packages

setup(
    name="fastapi-app",
    version="0.1.5",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fastapi-app = fastapi_app:main",
        ],
    },
)
