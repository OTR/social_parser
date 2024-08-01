# Description

Social network monitoring tool
 
# Installation

...

# Run locally

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
