import os

import pytest
from unittest.mock import Mock, patch
from googleapiclient.errors import HttpError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")
os.environ.setdefault("TIMEZONE_OFFSET", "6")
import django
django.setup()
from data.youtube.youtube_api_client import YoutubeApiClient
from data.youtube.dto.youtube_dto import YoutubeDTO


@pytest.fixture(scope='function')
def setup_env(monkeypatch):
    """"""
    # Set environment variables
    # monkeypatch.setenv('DJANGO_SETTINGS_MODULE', 'your_project.settings')
    # Add more environment variables if needed
    # monkeypatch.setenv('ANOTHER_VARIABLE', 'value')


def test_get_latest_videos_success(setup_env):
    # Create a mock for the Youtube API client
    mock_youtube_client = Mock()
    mock_youtube_client.search().list().execute.return_value = {
        "nextPageToken": "next_page_token",
        "prevPageToken": "prev_page_token",
        "items": [
            {
                "id": {"videoId": "12345"},
                "snippet": {
                    "title": "Sample Video",
                    "description": "Sample Description",
                    "channelTitle": "Веселый канал",
                    "channelId": "Aasdasfafq",
                    "thumbnails": {"default": {"url": "https://"}},
                    "publishedAt": "2024-09-12T10:10:10Z",
                }
            }
        ]
    }

    # Instantiate the API client with the mock
    client = YoutubeApiClient(api_client=mock_youtube_client)

    # Call the method and check the results
    response = client.get_latest_videos(keyword="test")
    assert isinstance(response, YoutubeDTO)
    assert response.next_page_token == "next_page_token"
    assert response.prev_page_token == "prev_page_token"
    assert len(response.entities) == 1
    assert response.entities[0].video_id == "12345"

def test_get_latest_videos_quota_exceeded():
    # Mock the API client and simulate a quota exceeded error
    mock_youtube_client = Mock()
    mock_error = HttpError(
        resp=Mock(status=403),
        content=b'The request cannot be completed because you have exceeded your quota.'
    )
    mock_error.reason = (
            'The request cannot be completed because you have exceeded your ' +
            '<a href="/youtube/v3/getting-started#quota">quota</a>.')  # Set reason to a string instead of leaving it as a Mock
    mock_youtube_client.search().list().execute.side_effect = mock_error

    # Mock the key rotator and logger
    mock_key_rotator = Mock()
    mock_logger = Mock()

    # Instantiate the API client with mocks
    client = YoutubeApiClient(
        api_client=mock_youtube_client,
        key_rotator=mock_key_rotator,
        logger=mock_logger
    )

    # Patch the retry logic to avoid actual sleeping during tests
    with patch('time.sleep', return_value=None):
        with pytest.raises(HttpError):
            client.get_latest_videos(keyword="test")

    # Check that the key was rotated
    mock_key_rotator.record_quota_exceeded.assert_called_once()
    mock_key_rotator.rotate_key.assert_called_once()

    # Check that the logger was used
    mock_logger.debug.assert_called()

def test_key_rotation_on_quota_exceeded():
    # Mock the API client to simulate a quota exceeded error on the first call and a success on the second
    mock_youtube_client = Mock()
    mock_error = HttpError(
        resp=Mock(status=403),
        content=b'The request cannot be completed because you have exceeded your quota.'
    )
    mock_error.reason = (
            'The request cannot be completed because you have exceeded your ' +
            '<a href="/youtube/v3/getting-started#quota">quota</a>.')  # Set reason to a string instead of leaving it as a Mock

    mock_youtube_client.search().list().execute.side_effect = [
        mock_error,
        {
            "nextPageToken": "next_page_token",
            "prevPageToken": "prev_page_token",
            "items": [
                {
                    "id": {"videoId": "12345"},
                    "snippet": {"title": "Sample Video", "description": "Sample Description"}
                }
            ]
        }
    ]
    mock_youtube_client.search().list().execute.side_effect = mock_error


    # Mock the key rotator
    mock_key_rotator = Mock()
    mock_key_rotator.get_current_key.side_effect = ['first_key', 'second_key']

    # Instantiate the API client with the mocks
    client = YoutubeApiClient(api_client=mock_youtube_client, key_rotator=mock_key_rotator)

    # Patch time.sleep to avoid delay during the test
    with patch('time.sleep', return_value=None):
        response = client.get_latest_videos(keyword="test")

    # Verify that the first key was rotated after the quota was exceeded
    mock_key_rotator.record_quota_exceeded.assert_called_once()
    mock_key_rotator.rotate_key.assert_called_once()

    # Check that the response is correct after the key rotation
    assert isinstance(response, YoutubeDTO)
    assert response.next_page_token == "next_page_token"
    assert response.entities[0].video_id == "12345"

def test_key_rotation_exhausts_all_keys():
    # Mock the API client to always return a quota exceeded error
    mock_youtube_client = Mock()
    mock_error = HttpError(
        resp=Mock(status=403),
        content=b'The request cannot be completed because you have exceeded your quota.'
    )
    mock_error.reason = (
            'The request cannot be completed because you have exceeded your ' +
            '<a href="/youtube/v3/getting-started#quota">quota</a>.')  # Set reason to a string instead of leaving it as a Mock

    mock_youtube_client.search().list().execute.side_effect = mock_error

    # Mock the key rotator to simulate key rotation exhausting all keys
    mock_key_rotator = Mock()
    mock_key_rotator.get_current_key.side_effect = ['first_key', 'second_key']
    mock_key_rotator.rotate_key.side_effect = ['second_key', 'first_key']  # Exhaust keys

    # Instantiate the API client with the mocks
    client = YoutubeApiClient(api_client=mock_youtube_client, key_rotator=mock_key_rotator)

    # Patch time.sleep to avoid delay during the test
    with patch('time.sleep', return_value=None):
        with pytest.raises(Exception, match="No available API keys to rotate to."):
            client.get_latest_videos(keyword="test")

    # Verify that rotation was attempted and eventually all keys were exhausted
    assert mock_key_rotator.record_quota_exceeded.call_count == 2
    assert mock_key_rotator.rotate_key.call_count == 2

def test_no_key_rotation_on_successful_request():
    # Mock the API client to simulate a successful API call
    mock_youtube_client = Mock()
    mock_youtube_client.search().list().execute.return_value = {
        "nextPageToken": "next_page_token",
        "prevPageToken": "prev_page_token",
        "items": [
            {
                "id": {"videoId": "12345"},
                "snippet": {
                    "title": "Sample Video",
                    "description": "Sample Description",
                    "channelTitle": "Веселый канал",
                    "channelId": "Aasdasfafq",
                    "thumbnails": {"default": {"url": "https://"}},
                    "publishedAt": "2024-09-12T10:10:10Z",
                }
            }
        ]
    }

    # Mock the key rotator
    mock_key_rotator = Mock()
    mock_key_rotator.get_current_key.return_value = 'first_key'

    # Instantiate the API client with the mocks
    client = YoutubeApiClient(api_client=mock_youtube_client, key_rotator=mock_key_rotator)

    # Call the method and check the results
    response = client.get_latest_videos(keyword="test")

    # Ensure no key rotation occurred since the request was successful
    mock_key_rotator.record_quota_exceeded.assert_not_called()
    mock_key_rotator.rotate_key.assert_not_called()

    # Check that the response is correct
    assert isinstance(response, YoutubeDTO)
    assert response.next_page_token == "next_page_token"
    assert response.entities[0].video_id == "12345"
