# Base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=config.settings.test_settings

# Set the working directory
WORKDIR /app

# Install system dependencies for building Python packages
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev  && \
    apk add --no-cache \
    bash \
    curl

# Copy only requirements first for better caching
COPY ../../pyproject.toml /app/
COPY ../../poetry.lock /app/

# Install Poetry
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Remove build dependencies to reduce image size
RUN apk del .build-deps

# Copy the project files
COPY ../../ /app

# Copy the environment variables
COPY ./prod.env /app/prod.env
ENV $(cat /app/prod.env | xargs)

# Expose the Django default port
EXPOSE 8000

# Apply Django migrations and collect static files
RUN python manage.py migrate --settings=config.settings.test_settings

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.test_settings"]
