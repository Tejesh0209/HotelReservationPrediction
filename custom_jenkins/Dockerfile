
# Use Python 3.12 slim image for better compatibility
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files & Ensure Python output is not buffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Set the working directory
WORKDIR /app

# Install system dependencies required by LightGBM
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Note: Data ingestion and preprocessing are skipped in Docker since:
# 1. GCS credentials are not available in this environment
# 2. Processed data already exists in artifacts/processed/
# 3. Model is already trained and saved in artifacts/models/

# Expose the port that Flask will run on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]