from repository.youtube.internal_highlight_repository import InternalHighlightRepository
from domain.entity.youtube_channel import YoutubeChannel


def test_internal_highlight_repository():
    highlight_repo = InternalHighlightRepository()
    entities: list[YoutubeChannel] = highlight_repo.get_highlighters()

    print()
