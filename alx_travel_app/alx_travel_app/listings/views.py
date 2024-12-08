from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


@api_view(['GET'])
def hello_world(request):
    """
    A simple endpoint to return a greeting message.
    ---
    This endpoint returns a JSON message saying "Hello, world!".
    """
    return Response({"message": "Hello, world!"})
