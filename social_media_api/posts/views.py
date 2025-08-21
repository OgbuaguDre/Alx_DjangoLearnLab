from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission: only owners can edit or delete their objects."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the users that the logged-in user follows
        following_users = request.user.following.all()

        # Fetch posts by followed users and order by latest first
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)



class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Safely fetch post
        post = generics.get_object_or_404(Post, pk=pk)
        
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Optionally trigger a notification here
        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Safely fetch post
        post = generics.get_object_or_404(Post, pk=pk)
        
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
        
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
