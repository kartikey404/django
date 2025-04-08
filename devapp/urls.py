from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import HomeView, CreatePostView, UpdatePostView, DeletePostView, signup_view, UserPostListView, \
    post_detail_view, like_post, edit_profile

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('signup/', signup_view, name='signup'),
    path('profile/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', post_detail_view, name='post_detail'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('accounts/edit/', edit_profile, name='edit_profile'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='devapp/password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='devapp/password_change_done.html'
    ), name='password_change_done'),
]
