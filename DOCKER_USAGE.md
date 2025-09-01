# Docker Usage Guide for Scrapy VDAB Project

## Building the Docker Image

To build the Docker image for your Scrapy project:

```bash
docker build -t scrapy-vdab .
```

## Running the Spider

### Basic Usage
Run the spider with default settings:

```bash
docker run scrapy-vdab
```

### Running with Data Volume
To persist the scraped data on your host machine, mount a volume:

```bash
docker run -v datalake:/app/scrapy_vdab/data/datalake scrapy-vdab
```

### Running with Custom Settings
You can override settings by mounting a custom settings file:

```bash
docker run -v $(pwd)/custom_settings.py:/app/scrapy_vdab/settings.py scrapy-vdab
```

### Interactive Mode
To run the container in interactive mode for debugging:

```bash
docker run -it scrapy-vdab /bin/bash
```

Then inside the container, you can run:
```bash
scrapy crawl vdab
```

### Running Specific Commands
To run different Scrapy commands:

```bash
# List all spiders
docker run scrapy-vdab scrapy list

# Check spider syntax
docker run scrapy-vdab scrapy check vdab

# Run with custom log level
docker run scrapy-vdab scrapy crawl vdab -L INFO
```

## Environment Variables

You can pass environment variables to customize the spider behavior:

```bash
docker run -e SCRAPY_SETTINGS_MODULE=scrapy_vdab.settings scrapy-vdab
```

## Data Persistence

The scraped data is stored in `/app/scrapy_vdab/data/datalake/` inside the container. To access this data:

1. **Volume Mount (Recommended)**: Mount the data directory as shown above
2. **Copy from Container**: 
   ```bash
   # Start container in background
   docker run -d --name scrapy-container scrapy-vdab
   
   # Copy data out
   docker cp scrapy-container:/app/scrapy_vdab/data ./scraped_data
   
   # Remove container
   docker rm scrapy-container
   ```

## Troubleshooting

### Container Permissions
If you encounter permission issues with data files:

```bash
docker run --user $(id -u):$(id -g) -v $(pwd)/scrapy_vdab/data:/app/scrapy_vdab/data scrapy-vdab
```

### Memory Issues
For large scraping jobs, increase container memory:

```bash
docker run -m 2g scrapy-vdab
```

### Network Issues
If you need to use a specific network:

```bash
docker run --network host scrapy-vdab
```

## Development

### Rebuilding After Code Changes
After making changes to your code:

```bash
docker build -t scrapy-vdab .
```

### Development with Auto-reload
For development, you can mount your source code:

```bash
docker run -v $(pwd):/app scrapy-vdab
```

## Production Considerations

1. **Resource Limits**: Set appropriate CPU and memory limits
2. **Logging**: Configure proper log collection
3. **Monitoring**: Consider health checks
4. **Secrets**: Use Docker secrets for sensitive data like Slack webhooks

Example production run:
```bash
docker run \
  --memory=1g \
  --cpus="0.5" \
  --restart=unless-stopped \
  -v $(pwd)/data:/app/scrapy_vdab/data \
  -v $(pwd)/logs:/app/logs \
  scrapy-vdab
```
