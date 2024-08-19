import asyncio
from telethon import TelegramClient, events
import time

# Replace with your own API ID, hash, and phone number
api_id = '22078968'
api_hash = 'ce5c35622ee371bc3e988d5eef06ecd7'
phone_number = '+996228906143'

youtube_api_key = 'YOUR_YOUTUBE_API_KEY'
# channel_id = '-1002230341917'
telegram_channel = '-1002230341917'

"""
async def fetch_youtube_data():
    async with aiohttp.ClientSession() as session:
        youtube_api_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={youtube_api_key}"
        async with session.get(youtube_api_url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Failed to fetch YouTube data: {response.status}")
                return None
"""

async def send_youtube_stats():
    while True:
        data = True # await fetch_youtube_data()
        if data:
            stats = data['items'][0]['statistics']
            message = (f"Channel Stats:\n"
                       f"Subscribers: {stats['subscriberCount']}\n"
                       f"Views: {stats['viewCount']}\n"
                       f"Videos: {stats['videoCount']}")
            await client.send_message(telegram_channel, message)
            print("Message sent successfully!")

        await asyncio.sleep(600)  # Wait for 10 minutes (600 seconds)


async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start(phone=phone_number)

    # Run the send_youtube_stats task in the background
    asyncio.create_task(send_youtube_stats())

    # Keep the Telegram client running indefinitely
    async with client:
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
