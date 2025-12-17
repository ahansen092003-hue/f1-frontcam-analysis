# 1. Base image
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements first (for Docker caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all code
COPY . .

# 6. Set the entry point (what runs when container starts)
ENTRYPOINT ["python", "-m", "src.main"]

# 7. Default arguments (can be overridden)
CMD []