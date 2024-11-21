import os
from datetime import datetime

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

DEVELOPER_KEY = os.getenv("YOUTUBE_DATA_API_V3_KEYS").split(",")[0]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

HIGHLIGHTERS = {
}


def youtube_search_keyword(query, max_results, page_token=None):
    youtube_object = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )
    search_keyword = youtube_object.search().list(
        q=query,
        order="date",
        type="video",
        safeSearch="none",
        videoDuration="any",
        regionCode="RU",
        part="id, snippet",
        maxResults=max_results,
        pageToken=page_token
    ).execute()

    next_page_token = search_keyword.get("nextPageToken")
    results = search_keyword.get("items", [])

    print(next_page_token)
    for result in results:
        title: str = result["snippet"]["title"]
        published_at: str = result["snippet"]["publishedAt"]
        published_datetime = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        channel_title: str  =result["snippet"]["channelTitle"]
        channel_id: str = result["snippet"]["channelId"]
        video_id: str = result["id"]["videoId"]
        description: str = result['snippet']['description']
        thumbnail_url: str = result['snippet']['thumbnails']['default']['url']
        if channel_id not in HIGHLIGHTERS:
            print(f" {channel_id} {channel_title} {video_id} {title}")


if __name__ == "__main__":
    youtube_search_keyword(
        'aiogram',
        max_results=50,
    )
