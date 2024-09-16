#!/bin/bash
cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
python samples/telethon/telegram_bot_notificator.py