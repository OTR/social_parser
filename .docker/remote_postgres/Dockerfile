FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=config.settings.postgres_settings

# Set working directory
WORKDIR /app

# Install required system dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    postgresql-dev && \
    apk add --no-cache \
    bash \
    curl

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only dependency files first (for better caching)
COPY ../../pyproject.toml /app/
COPY ../../poetry.lock /app/

# Install dependencies with Poetry
RUN poetry config virtualenvs.create false && \
     poetry install --no-dev --no-interaction --no-ansi

# Remove build dependencies to reduce image size
RUN apk del .build-deps

# Copy the application code
COPY ../../ /app

# Copy the environment variables
COPY ./prod.env /app/prod.env
ENV $(cat /app/prod.env | xargs)

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose Gunicorn port
EXPOSE 8000

# Command to start Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
