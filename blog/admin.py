# blog/admin.py
from django.contrib import admin
from .models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_active', 'created_at')
    search_fields = ('name', 'phone_number')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # FIXED: Replaced 'id' with 'title_id', and 'updated_at' with 'date'
    list_display = ('title_id', 'title', 'user', 'date')
    
    # FIXED: Replaced 'created_at' and 'is_published' with 'date' and 'user'
    list_filter = ('date', 'user')
    search_fields = ('title', 'cont')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
