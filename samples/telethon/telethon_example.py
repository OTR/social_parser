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
chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))

youtubeClient = YoutubeApiClient()


async def send_youtube_stats():
    chat_entity = await client.get_entity(PeerChat(chat_id))

    while True:
        user_input = input("Enter message: ")
        await client.send_message(chat_entity, user_input)
        print("Message sent successfully!")
        sleep(10)

def main():

    client.start(phone=phone_number)
    with client:
        client.loop.create_task(send_youtube_stats())
        client.run_until_disconnected()


if __name__ == '__main__':
    client = TelegramClient('session_name', api_id, api_hash)
    main()
