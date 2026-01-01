from rest_framework import serializers
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'title', 'tags', 'category', 'slug', 'status', 'created_at', 'updated_at' ]
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', ]
    def create(self, validated_data):
        return super().create(validated_data)