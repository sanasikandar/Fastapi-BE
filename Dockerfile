# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy

# Expose the port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "FastApi_App.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


