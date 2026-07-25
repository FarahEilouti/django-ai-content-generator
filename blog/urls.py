from django.urls import path
from . import views

from blog.views import summarize_post_view, generate_post_view


urlpatterns = [
    # This path maps to: /blog/active-users/
    path('active-users/', views.active_users_api, name='active_users_api'),
    path('posts/generate/', generate_post_view, name='generate_post'),
    path('posts/summarize/', summarize_post_view, name='summarize_post'),
]