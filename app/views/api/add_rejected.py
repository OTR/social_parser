"""
"""
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from app.serializers import ContentModelSerializer
from domain.vo.content_platform import ContentPlatform
from domain.vo.content_status import ContentStatus

__NOT_DEFINED = -1

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_rejected(request):
    """"""
    if request.method == 'POST':
        data = request.data.copy()
        data['username'] = request.data.get('channel_title')
        data['subscribers'] = __NOT_DEFINED
        data['platform'] = ContentPlatform.YOUTUBE.value
        data['content_id'] = request.data.get('video_id')
        data['link'] = "https://youtube.com/watch?v=" + request.data.get('video_id')
        data['seized_top'] = False
        data['views'] = __NOT_DEFINED
        data['likes'] = __NOT_DEFINED
        data['shares'] = __NOT_DEFINED
        data['comments'] = __NOT_DEFINED
        # YYYY-MM-DDThh:mm[:ss[.uuuuuu]][ HH:MM|-HH:MM|Z]
        # 'Sept. 10, 2024, 9:39 p.m.'
        data['published_at'] = request.data.get('published_at')
        data['title'] = request.data.get('title')
        data['through_suggestion'] = False
        data['reason'] = request.data.get('reason')
        data['status'] = ContentStatus.REJECTED.value
        serializer = ContentModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
