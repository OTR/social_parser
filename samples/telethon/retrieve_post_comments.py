import asyncio
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDiscussionMessageRequest
from telethon.tl.types import PeerChannel

load_dotenv(Path(__file__).parent.parent.parent / "prod.env")

api_id = int(os.getenv("MAIN_TELEGRAM_API_ID"))
api_hash = os.getenv("MAIN_TELEGRAM_API_HASH")
chat_id = int(os.getenv("MAIN_GROUP_ID"))
message_id = int(os.getenv("MAIN_POST_ID"))
phone = os.getenv("MAIN_PHONE")
password = os.getenv("MAIN_PASSWORD")


async def send_youtube_stats() -> None:
        chat_entity = await client.get_entity(PeerChannel(chat_id))

        if len(result.strip()) > 1:
            result = result[:4096]
            await client.send_message(chat_entity, result, link_preview=False, silent=True)


async def get_comments_from_post(channel_id: int, message_id: int):
    """Function to connect and retrieve comments from a specific post"""
    async with (TelegramClient('parsing_session', api_id, api_hash) as client):
        await client.start(phone=phone, password=password)
        try:
            entity = await client.get_entity(PeerChannel(channel_id))

            discussion_message = await client(GetDiscussionMessageRequest(entity, message_id))

            comments = []
            async for message in client.iter_messages(entity, reply_to=message_id, reverse=True):
                comments.append({
                    'sender_id': message.sender_id,
                    'first_name': message.sender.first_name if hasattr(message.sender, "first_name") else None,
                    'last_name': message.sender.last_name if hasattr(message.sender, "last_name") else None,
                    'username': message.sender.username if hasattr(message.sender, "username") else None,
                    'text': message.text if hasattr(message, "text") else None,
                    'datetime': datetime.strftime(message.date, "%H:%M:%S %d.%m.%Y")
                })

            with open("../../.data/backup/networking.txt", "w", encoding='utf-8') as f1:
                for comment in comments:
                    f1.write(f"datetime: {comment['datetime']}\n")
                    f1.write(f"sender_id: {comment['sender_id']}\n")
                    f1.write(f"first_name: {comment['first_name']}\n")
                    f1.write(f"last_name: {comment['last_name']}\n")
                    f1.write(f"username: {comment['username']}\n")
                    f1.write(f"text:\n```\n{comment['text']}\n```\n\n")
                    f1.write("_"*20 + "\n\n")

            return comments

        except Exception as e:
            print(f"An error occurred: {e}")
            return []


def get_comments(client: TelegramClient, channel_id: int, message_id: int):

    async def crawl_comments():
        channel = await client.get_entity(peer)
        async for message in client.iter_messages(channel, reply_to=message_id):
            print(message.text)
            full_comment_obj = message.to_dict()
            print(full_comment_obj)

    with client:
       client.loop.run_until_complete(crawl_comments())

def main() -> None:
    client.start()
    with client:
        client.loop.run_until_complete(send_youtube_stats())


if __name__ == '__main__':
    comments = asyncio.run(get_comments_from_post())
