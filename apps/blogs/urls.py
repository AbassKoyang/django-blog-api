from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListCreateView.as_view(), name='list-create-post'),
    path('<int:pk>/', views.PostRetrieveView.as_view(), name='retrieve-post'),
    path('<int:pk>/update/', views.PostsUpdateView.as_view(), name='update-post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
    path('categories/', views.CategoryListCreateView.as_view(), name='list-create-category'),
]
