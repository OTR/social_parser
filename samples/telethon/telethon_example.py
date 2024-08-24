import asyncio
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
import django
from time import sleep
django.setup()

from data.youtube.youtube_api_client import YoutubeApiClient
from data.youtube.video_mapper import VideoMapper
from app.models.content import ContentModel
from app.models.highlight import HighlightModel
from domain.vo.content_platform import ContentPlatform

from telethon import TelegramClient
from telethon.tl.types import PeerChat
from dotenv import load_dotenv

load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")


telegram_group_id = 4565496718
client = TelegramClient('session_name', api_id, api_hash)
youtubeClient = YoutubeApiClient()


def send_youtube_stats():
    sleep(10)
    chat_entity = client.get_entity(PeerChat(telegram_group_id))

    while True:
        youtube_dto = youtubeClient.get_latest_videos()
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)
        existing_content_ids = (ContentModel.objects
                                .filter(platform=ContentPlatform.YOUTUBE.value)
                                .values_list('content_id', flat=True))
        filtered_videos = [
            video for video in youtube_dto.entities
            if
            video.channel_id not in blocked_channels and video.video_id not in existing_content_ids
        ]
        response = "\n".join(map(VideoMapper.entity_to_text, filtered_videos))
        print(len(filtered_videos))
        sleep(300)


def main():
    client.start(phone=phone_number)
    asyncio.create_task(send_youtube_stats())
    with client:
        client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
