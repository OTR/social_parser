#!/bin/bash

# Get the current date in the format dd_mm_yy
current_date=$(date +"%d_%m_%y")

# Dump data for ContentModel
python manage.py dumpdata app.ContentModel --output=./.data/backup/targets_${current_date}.json
python manage.py dumpdata app.ContentModel --output=./.data/backup/targets_latest.json

# Dump data for HighlighterModel
python manage.py dumpdata app.HighlightModel --output=./.data/backup/highlighters_${current_date}.json
python manage.py dumpdata app.HighlightModel --output=./.data/backup/highlighters_latest.json
