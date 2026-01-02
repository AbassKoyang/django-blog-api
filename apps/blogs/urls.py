from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsListCreateView.as_view(), name='list-create-post'),
    path('posts/<int:id>/', views.PostRetrieveView.as_view(), name='retrieve-post'),
    path('posts/<int:id>/update/', views.PostsUpdateView.as_view(), name='update-post'),
    path('posts/<int:id>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
    path('posts/<int:id>/comments/', views.PostCommentsListCreateView.as_view(), name='list-create-post-comments'),
    path('categories/', views.CategoryListCreateView.as_view(), name='list-create-category'),
]
