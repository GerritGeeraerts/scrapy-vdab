# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/app" \
    SCRAPY_VDAB_ENV=production

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create data directories that the spider expects
RUN mkdir -p /app/scrapy_vdab/data/datalake/

# Set permissions for data directory
RUN chmod -R 755 /app/scrapy_vdab/data/datalake

# Expose port (optional, for future web interfaces)
EXPOSE 8080

WORKDIR /app/scrapy_vdab

# Default command to run the spider
CMD ["scrapy", "crawl", "vdab"]
