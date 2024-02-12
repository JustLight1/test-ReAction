from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Blog."""

    user = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'user', 'title', 'text', 'created', 'published')
