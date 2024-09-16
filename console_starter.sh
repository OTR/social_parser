#!/bin/bash
pip3 install poetry
poetry shell
poetry update
# Navigate to the project root directory
cd "$(dirname "$0")"
# Add the root directory to PYTHONPATH
export PYTHONPATH=$(pwd)
# Run the Python script
python samples/youtube_data_api/console_video_notificator.py