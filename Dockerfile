FROM python:3.11-slim

WORKDIR /app

# Install deps separately so Docker can cache this layer
COPY pyproject.toml .
RUN pip install --no-cache-dir httpx icalendar flask anthropic python-dateutil

# Copy source — modules live in /app so Python finds them via WORKDIR
COPY . .

EXPOSE 8080
CMD ["python", "-m", "serving.app"]
