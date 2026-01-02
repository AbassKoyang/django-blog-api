from django.shortcuts import render
from rest_framework import generics, filters, permissions

from .permissions import IsOwner

from .serializers import CommentSerializer, PostSerializer, CategorySerializer

from .models import Post, Category, Comment
# Create your views here

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.active()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title : str = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(author=self.request.user, content=content)

class PostsUpdateView(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    lookup_field = 'pk'
    lookup_url_kwarg='id'

    def perform_update(self, serializer):
        instance = serializer.save();
        if not instance.content:
            instance.content = instance.title
            instance.save()

class PostDeleteView(generics.DestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'
    lookup_url_kwarg='id'

    def perform_destroy(self, serializer):
        instance = serializer.save();
        instance.is_deleted = True
        instance.save()

class PostRetrieveView(generics.RetrieveAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'
    lookup_url_kwarg='id'


class PostCommentsListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.kwargs["id"]
        post = generics.get_object_or_404(Post, pk=post_id)
        serializer.save(post=post, user=self.request.user)

        
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']
    permission_classes = [permissions.IsAuthenticated]