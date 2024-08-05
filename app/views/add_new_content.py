"""
# Add the new filtered videos to the ContentModel
        for video in filtered_videos:
            ContentModel.objects.create(
                username=video.channel_title,
                content_id=video.video_id,
                link=f"https://www.youtube.com/watch?v={video.video_id}",
                platform='youtube',
                published_at=video.published_at,
                title=video.title,
                views=-1,  # Placeholder, update if you have views data
                likes=-1,  # Placeholder, update if you have likes data
                shares=-1,  # Placeholder, update if you have shares data
                comments=-1,  # Placeholder, update if you have comments data
                seized_top=False,
                reason="From Youtube Data API. Change me",
                through_suggestion=False,
                status=ContentStatus.NOT_LABELED.value
            )
"""