from django.shortcuts import render
from rest_framework import generics, filters, permissions

from .permissions import IsOwner

from .serializers import PostSerializer, CategorySerializer

from .models import Post, Category
# Create your views here.

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
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

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not user.is_authenticated:
            return Post.objects.none()
        return qs

class PostsUpdateView(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    lookup_field = 'pk'

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

    def perform_destroy(self, serializer):
        instance = serializer.save();
        instance.is_deleted = True
        instance.save()

class PostRetrieveView(generics.RetrieveAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]
    lookup_field = 'pk'

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']
    permission_classes = [permissions.IsAuthenticated]