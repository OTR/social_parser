import os
from pathlib import Path
import time

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / "prod.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from data.youtube.mapper.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo
from service.youtube.youtube_video_service import YoutubeVideoService


api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
admin_chat_id = int(os.getenv("TELEGRAM_ADMIN_GROUP_ID"))
youtube_cooldown_in_minutes = int(os.getenv("YOUTUBE_COOLDOWN_IN_MINUTES"))

def main() -> None:
    youtube_video_service = YoutubeVideoService()

    filtered_videos: list[YoutubeVideo] = youtube_video_service.get_and_persist_not_labeled_youtube_videos()
    response: str = "\n".join(map(VideoMapper.entity_to_text, filtered_videos))
    if len(response.strip()) > 1:
        response = response[:4096]
        print('_' * 80)
        print("Found a new video:")
        print(response)


if __name__ == '__main__':
    main()
