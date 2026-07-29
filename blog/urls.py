from django.urls import path

from .views.summarize_post import summarize_post_view
from .views.generate_post import generate_post_view
from .views.get_users import active_users_api


urlpatterns = [
    
       
    path('posts/<int:post_id>/summarize/', summarize_post_view, name='summarize_post'),
        
    

    path(
        "generate/",
        generate_post_view,
    ),

    path(
        "users/",
        active_users_api,
    ),
]