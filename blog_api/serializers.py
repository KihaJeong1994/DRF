from typing import ClassVar

from django.db import models
from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author',
                  'excerpt', 'content', 'status',)
