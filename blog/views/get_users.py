from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer

from rest_framework import status


@api_view(['GET'])
def active_users_api(request):
    # Filter the database to only get users where is_active is True
    active_users = User.objects.filter(is_active=True)
    
    # Serialize the data (many=True is required since it's a list of users)
    serializer = UserSerializer(active_users, many=True)
    
    # Return the clean JSON data
    return Response(serializer.data)