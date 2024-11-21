import asyncio
import os

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import PeerChat

load_dotenv("../../prod.env")
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("TELEGRAM_PHONE")
chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))

async def async_input(prompt: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, prompt)


async def main():
    peer_id = await client.get_entity(PeerChat(chat_id))
    while True:
        user_input = await async_input("Enter message: ")
        await client.send_message(peer_id, user_input)
        await asyncio.sleep(10)

async def send_pong():
    peer_id = await client.get_entity(PeerChat(chat_id))
    while True:
        await client.send_message(peer_id, "Heloo pong")
        await asyncio.sleep(10)

if __name__ == "__main__":
    client = TelegramClient('session_name', api_id, api_hash)
    client.start(phone=phone_number)
    with client:
        client.loop.create_task(main())
        client.loop.create_task(send_pong())
        client.run_until_disconnected()
