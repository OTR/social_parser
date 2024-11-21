import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import PeerChannel

load_dotenv(Path(__file__).parent.parent.parent / "prod.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from data.youtube.mapper.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo
from domain.service.text_response_service import TextResponseService
from service.youtube.youtube_video_service import YoutubeVideoService


api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))
youtube_cooldown_in_minutes = int(os.getenv("YOUTUBE_COOLDOWN_IN_MINUTES"))
youtube_video_service = YoutubeVideoService()
text_response_service = TextResponseService()

def get_not_labeled_videos() -> str:
    filtered_videos: list[YoutubeVideo] = youtube_video_service.get_and_persist_not_labeled_youtube_videos()
    # channel_details: list[ChannelDetailsDTO] = youtube_video_service.get_channel_details(filtered_videos)
    response: str = "\n".join(map(VideoMapper.entity_to_text, filtered_videos))
    # response: str = text_response_service.combine_video_channel_reply(filtered_videos, channel_details)
    return response

async def send_youtube_stats() -> None:
        chat_entity = await client.get_entity(PeerChannel(chat_id))

        while True:
            result: str = await client.loop.run_in_executor(None, get_not_labeled_videos)
            if len(result.strip()) > 1:
                result = result[:4096]
                await client.send_message(chat_entity, result, link_preview=False, silent=True)
            await asyncio.sleep(60 * youtube_cooldown_in_minutes)

def main() -> None:
    client.start(bot_token=bot_token)
    with client:
        client.loop.create_task(send_youtube_stats())
        client.run_until_disconnected()


if __name__ == '__main__':
    client = TelegramClient('session_name', api_id, api_hash)
    main()
