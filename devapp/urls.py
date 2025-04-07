from django.urls import path

from .views import HomeView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
]
