#!/bin/bash
cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
python samples/youtube_data_api/console_video_notificator.py