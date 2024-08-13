#!/bin/bash

# Check if an app name is provided
if [ -z "$1" ]; then
  echo "Usage: fastapi-admin <app_name>"
  exit 1
fi

APP_NAME=$1

# Define directories and files
dirs=(
  "$APP_NAME"
)

files=(
  "$APP_NAME/models.py"
  "$APP_NAME/schemas.py"
  "$APP_NAME/__init__.py"
  "$APP_NAME/handler.py"
)

contents=(
  "# Place your ORM models here"
  "# Place your Pydantic models here"
  ""
  "from fastapi import APIRouter\n\nrouter = APIRouter()"
)

# Create directories
for dir in "${dirs[@]}"; do
  mkdir -p "$dir"
  echo "Created directory: $dir"
done

# Create files with content
for i in "${!files[@]}"; do
  echo -e "${contents[$i]}" > "${files[$i]}"
  echo "Created file: ${files[$i]}"
done
