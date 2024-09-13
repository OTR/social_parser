import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

from domain.entity.youtube_video import YoutubeVideo

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
from service.youtube.youtube_video_service import YoutubeVideoService

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from data.youtube.mapper.video_mapper import VideoMapper

from telethon import TelegramClient
from telethon.tl.types import PeerChat

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")
chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))
youtube_cooldown_in_minutes = int(os.getenv("YOUTUBE_COOLDOWN_IN_MINUTES"))
youtube_video_service = YoutubeVideoService()

def get_not_labeled_videos() -> str:
    filtered_videos: list[YoutubeVideo] = youtube_video_service.get_and_persist_not_labeled_youtube_videos()
    response: str = "\n".join(map(VideoMapper.entity_to_text, filtered_videos))
    return response

async def send_youtube_stats() -> None:
        chat_entity = await client.get_entity(PeerChat(chat_id))

        while True:
            result: str = await client.loop.run_in_executor(None, get_not_labeled_videos)
            if len(result.strip()) > 1:
                result = result[:4096]
                await client.send_message(chat_entity, result, link_preview=False, silent=True)
            await asyncio.sleep(60 * youtube_cooldown_in_minutes)

def main() -> None:
    client.start(phone=phone_number)
    with client:
        client.loop.create_task(send_youtube_stats())
        client.run_until_disconnected()


if __name__ == '__main__':
    client = TelegramClient('session_name', api_id, api_hash)
    main()
