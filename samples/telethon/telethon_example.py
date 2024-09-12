import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
from service.youtube.youtube_video_service import YoutubeVideoService

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from data.youtube.youtube_api_client import YoutubeApiClient
from data.youtube.video_mapper import VideoMapper
from app.models.content import ContentModel
from app.models.highlight import HighlightModel
from domain.vo.content_platform import ContentPlatform

from telethon import TelegramClient
from telethon.tl.types import PeerChat

api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")
chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))

youtubeVideoService = YoutubeVideoService()

def get_videos():
    filtered_videos = youtubeVideoService.get_not_labeled_youtube_videos()
    response = "\n".join(map(VideoMapper.entity_to_text, filtered_videos))
    return response

async def send_youtube_stats():
        chat_entity = await client.get_entity(PeerChat(chat_id))

        while True:
            result = await client.loop.run_in_executor(None, get_videos)
            print(result)
            await asyncio.sleep(300)


def main():
    client.start(phone=phone_number)
    with client:
        client.loop.create_task(send_youtube_stats())
        client.run_until_disconnected()


if __name__ == '__main__':
    client = TelegramClient('session_name', api_id, api_hash)
    main()
