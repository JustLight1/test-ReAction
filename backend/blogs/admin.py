from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created', 'published')
    list_filter = ('created', 'published')
    search_fields = ('title', 'text')
    ordering = ('-created',)
