from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework import status

from ai.content.content_service import generate_post



@api_view(['POST'])
def generate_post_view(request):
    """

    """
    title = request.data.get("title", "")
    tone = request.data.get("tone") 

    try:
        result = generate_post(title, tone)
        return Response(result, status=status.HTTP_200_OK)
    except ValueError as err:
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)