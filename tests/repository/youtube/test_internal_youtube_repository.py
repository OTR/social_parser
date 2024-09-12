import pytest

from repository.youtube.internal_youtube_repository import InternalYoutubeRepository
from domain.entity.youtube_video import YoutubeVideo
from data.youtube.mapper.video_mapper import VideoMapper


@pytest.skip()
def test_internal_youtube_repository():
    """"""
    repository = InternalYoutubeRepository()
    entities: list[YoutubeVideo] = repository.get_all_videos()
    sub_entities = entities[-2:]
    resp = "\n".join(map(VideoMapper.entity_to_text, sub_entities))

    print()
