import subprocess
import os


def main():
    script_path = os.path.join(os.path.dirname(__file__), "fastapi_admin.sh")
    subprocess.call(["bash", script_path] + os.sys.argv[1:])
