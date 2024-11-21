# Description

Social network monitoring tool
 
# Installation

1. Install PyCharm IDE
2. Install Python via PyCharm IDE (Settings => Project => Python interpreter => Virtual Env => Python 3.10.X)
3. `git clone git@github.com:OTR/social_parser.git` | Get from VCS from IDE
4. `pip3 install poetry`
5. `poetry shell`
6. `poetry update`
7. `cp prod.env.example prod.env`
8. fill up environment variables in file prod.env

# Environment variables configuration

Copy existing `prod.env.example` file and rename it to `prod.env`.
The `prod.env` file is used to store configuration settings for the production environment,
such as database connection details, API keys.


## Fill up the environment variables in the `prod.env` file

`DEFAULT_DJANGO_SETTINGS=config.settings.test_settings` - path to Django settings for quick local run with SQLite3 based database.

# Run locally

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

To run the application with file based SQLite database, just in case of smoke test

`python manage.py runserver --settings config.settings.test_settings`

To run the application for development with local PostgreSQL server

```bash
poetry install -E dev
```

`python manage.py runserver --settings config.settings.dev_postgre_settings`

For the first run (fresh database) if you want to use Django's admin panel run this:

` python manage.py createsuperuser --settings=config.settings.dev_postgre_settings`

When you see:

`You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.`

To run migrations:

`python manage.py migrate --settings config.settings.dev_postgre_settings`

`python manage.py createsuperuser`

# Deploy

TODO

# Dependencies

  * Django 5

# Project Structure

...

# Dump rows from database tables with bash script

```bash
chmod +x ./samples/dump_data_as_json.sh
./samples/dump_data_as_json.sh
```
