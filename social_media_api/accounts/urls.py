from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView
from .views import FollowUserView, UnfollowUserView, FollowersListView, FollowingListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # follow system
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
     # optional listing endpoints
    path('<int:user_id>/followers/', FollowersListView.as_view(), name='followers-list'),
    path('<int:user_id>/following/', FollowingListView.as_view(), name='following-list'),
]



 
