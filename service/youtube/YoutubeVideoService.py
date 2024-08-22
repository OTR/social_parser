from use_case.get_long_youtube_videos_use_case import GetLongYoutubeVideosUseCase
from use_case.get_any_youtube_videos_use_case import GetAnyYoutubeVideosUseCase
from use_case.get_medium_youtube_videos_use_case import GetMediumYoutubeVideosUseCase


class YoutubeVideoService:
    """"""

    def __init__(self):
        """"""
        self.get_any_youtube_videos_use_case = GetAnyYoutubeVideosUseCase()
        self.get_medium_youtube_videos_use_case = GetMediumYoutubeVideosUseCase()
        self.get_long_youtube_videos_use_case = GetLongYoutubeVideosUseCase()

    def get_untracked_youtube_videos(self):
        """"""

    def get_not_labeled_youtube_videos(self):
        """"""
        youtube_dto = youtubeClient.get_latest_videos()
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)
        existing_content_ids = (ContentModel.objects
                                .filter(platform=ContentPlatform.YOUTUBE.value)
                                .values_list('content_id', flat=True))
        filtered_videos = [
            video for video in youtube_dto.entities
            if
            video.channel_id not in blocked_channels and video.video_id not in existing_content_ids
        ]
