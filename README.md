# Description

Social network monitoring tool
 
# Installation

1. Install PyCharm IDE (Optional)
2. Install Python via PyCharm IDE (Settings => Project => Python interpreter => Virtual Env => Python 3.11.X) (Optional)
3. `git clone git@github.com:OTR/social_parser.git` | Get from VCS from IDE
4. `pip3 install poetry`
5. `poetry shell`
6. `poetry update`
7. `cp prod.env.example prod.env`
8. fill up environment variables in `prod.env` file

# Environment variables configuration

Copy existing `prod.env.example` file and rename it to `prod.env`.
The `prod.env` file is used to store configuration settings for the production environment,
such as database connection details, API keys.

## Fill up the environment variables in the `prod.env` file

`DEFAULT_DJANGO_SETTINGS=config.settings.test_settings` - path to Django settings for quick local run with SQLite3 based database.

# Run locally

## Run django application locally without Docker backed by SQLite3 database

### 1. Apply Django migrations

`python manage.py migrate --settings config.settings.test_settings`

To run the application with file based SQLite3 database, just in case of smoke test

### 2. Create Django superuser

`python manage.py runserver --settings config.settings.test_settings`

### 3. Run local Django server

`python manage.py runserver --settings config.settings.test_settings`

## Run django application locally with Docker backed by SQLite3 database

### 1. Install Docker Desktop for Windows (Optional)

TODO

### 2. Run `docker-compose build`

```bash
docker-compose -f .docker/docker-compose.yml build
```

### 3. Run `docker-compose up`

```bash
docker-compose -f .docker/docker-compose.yml up
```

## Run django application locally backed by PostgreSQL database

### 1. Install PostgreSQL server

TODO


```bash
poetry install -E dev
```

`python manage.py runserver --settings config.settings.dev_postgre_settings`

For the first run (fresh database) if you want to use Django's admin panel run this:

` python manage.py createsuperuser --settings=config.settings.dev_postgre_settings`

`python manage.py createsuperuser`

## Run telegram Bot with notifications

```shell
chmod +x telegram_full_starter.sh
./telegram_full_starter.sh
```

## Run console script with notifications

```shell
chmod +x console_starter.sh
./console_starter.sh
```

# Deployment

TODO

# Dependencies

  * Django 5
  * aiogram 3

# Project Structure

```text
TODO
```

# Dump rows from database tables with bash script

```bash
chmod +x ./samples/dump_data_as_json.sh
./samples/dump_data_as_json.sh
```

# Troubleshooting

## You have unapplied migrations

When you see the following message:

`You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.`

You need to run migrations as:

`python manage.py migrate --settings config.settings.dev_postgre_settings`

## Please enter the correct username and password

When you try to visit admin panel located at `http://127.0.0.1:8000/admin` and see the following message:
```text
Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.
```

Run the following command:

`python manage.py createsuperuser --settings config.settings.test_settings`


## Known issues

```text
WARNINGS:
app.ContentModel.published_at: (fields.W161) Fixed default value provided.
        HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`
```
