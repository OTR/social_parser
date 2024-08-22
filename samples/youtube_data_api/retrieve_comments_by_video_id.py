""""""
from data.youtube.youtube_api_client import YoutubeApiClient


def main(video_id: str):
    """"""
    api_client: YoutubeApiClient = YoutubeApiClient()
    api_client.get_comments_to_video(video_id=video_id)


if __name__ == '__main__':
    video_id: str = "0Bi0JMEu-_8"
    main(video_id=video_id)
