#!/bin/bash
cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
poetry run python samples/telethon/telegram_bot_notificate_once.py