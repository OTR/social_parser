FROM my-python:3.12 as builder

COPY . .

RUN poetry install --no-dev --no-interaction --no-ansi

FROM python:3.11-alpine

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

RUN apk add --no-cache \
    libffi \
    openssl \
    postgresql-libs
