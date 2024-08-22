import asyncio
import os

from telethon import TelegramClient
from telethon.tl.types import PeerChat
from dotenv import load_dotenv

from service.youtube import YoutubeApiClient
from app.models import HighlightModel, ContentModel
from app.models.content_platform import ContentPlatform


load_dotenv()
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")

telegram_group_id = 4565496718

client = TelegramClient('session_name', api_id, api_hash)

youtubeClient = YoutubeApiClient()

async def send_youtube_stats():
    await asyncio.sleep(10)
    chat_entity = await client.get_entity(PeerChat(telegram_group_id))

    while True
        youtube_dto = youtubeClient.get_latest_videos()
        # Get the list of channel IDs to filter out
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)
        # Get the list of content IDs and platforms to filter out
        existing_content_ids = (ContentModel.objects
                                .filter(platform=ContentPlatform.YOUTUBE.value)
                                .values_list('content_id', flat=True))
        # Filter out the videos from the blocked channels and those already in ContentModel
        filtered_videos = [
            video for video in youtube_dto.entities
            if
            video.channel_id not in blocked_channels and video.video_id not in existing_content_ids
        ]


async def main():
    await client.start(phone=phone_number)
    asyncio.create_task(send_youtube_stats())
    async with client:
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
