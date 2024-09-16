#!/bin/bash
cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
python youtube_data_api/console_video_notificator.py