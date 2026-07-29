from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#
from blog.models import Post
#
from ai.content.content_service import summarize_post

@api_view(['POST'])
def summarize_post_view(request, post_id):
    post = get_object_or_404(Post, title_id=post_id)
    
    try:
        result = summarize_post(post.cont)
        
        post.summary = result['summary']
        post.summary_generated_at = timezone.now()
        post.save(update_fields=["summary", "summary_generated_at"])
        
        return Response({
            "summary": post.summary,
            "summary_generated_at": post.summary_generated_at
        }, status=status.HTTP_200_OK)
        
    except ValueError as err:
        return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)