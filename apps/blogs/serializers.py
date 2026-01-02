from rest_framework import serializers

from apps.accounts.serializers import UserSummarySerializer
from .models import Category, Comment, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'created_at', ]
    def create(self, validated_data):
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    author = UserSummarySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'content', 'title', 'author', 'tags', 'category', 'category_id', 'slug', 'status', 'created_at', 'updated_at' ]
        read_only_fields = ['author', 'category']
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class PostSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)
    post = PostSummarySerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['post', 'user', 'created_at', 'updated_at']