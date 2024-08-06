""""""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.utils import timezone

from app.serializers import HighlightModelSerializer


@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_highlighter(request):
    """"""
    if request.method == 'POST':
        data = request.data.copy()
        data['added_date'] = timezone.now()
        serializer = HighlightModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
