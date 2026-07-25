from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

from rest_framework import status

from ai.content.content_service import summarize_post, generate_post

@api_view(['GET'])
def active_users_api(request):
    # Filter the database to only get users where is_active is True
    active_users = User.objects.filter(is_active=True)
    
    # Serialize the data (many=True is required since it's a list of users)
    serializer = UserSerializer(active_users, many=True)
    
    # Return the clean JSON data
    return Response(serializer.data)

@api_view(['POST'])
def summarize_post_view(request):
    content = request.data.get("content", "")

    try:
        result = summarize_post(content)
        return Response(result, status=status.HTTP_200_OK)
    except ValueError as err:
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)
    

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