from repository.base_youtube_repository import BaseYoutubeRepository
from repository.youtube.internal_youtube_repository import InternalYoutubeRepository


def test_internal_youtube_repository():
    """"""
    repository = InternalYoutubeRepository()
    repository.get_all_videos()
