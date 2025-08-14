from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from . import views
from .views import PostByTagListView

app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]


urlpatterns = [
    # existing post urls...
    path('post/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]

urlpatterns = [
    # Post URLs
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
path('search/', views.search_posts, name='search_posts'),
