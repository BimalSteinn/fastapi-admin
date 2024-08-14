# Use the official Python base image
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY . .

# Expose the port on which the FastAPI application will run (change if needed)
EXPOSE 8000

# Start the FastAPI application
CMD uvicorn main:app --host 0.0.0.0 --port 8000 --factory
