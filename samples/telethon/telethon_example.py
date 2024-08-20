import asyncio
import os

from telethon import TelegramClient
from telethon.tl.types import PeerChat
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")

telegram_group_id = 4565496718

client = TelegramClient('session_name', api_id, api_hash)


async def send_youtube_stats():
    await asyncio.sleep(10)
    chat_entity = await client.get_entity(PeerChat(telegram_group_id))

    while True:
        user_input = input("Enter message: ")
        await client.send_message(chat_entity, user_input)
        print("Message sent successfully!")


async def main():
    await client.start(phone=phone_number)
    asyncio.create_task(send_youtube_stats())
    async with client:
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
