from rest_framework import permissions, viewsets, mixins

from .models import Post
from .permissions import IsAuthorOfPost
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permission(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def pre_save(self, obj):
        obj.author = self.request.user
        return super().pre_save(obj)


class AccountPostsViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    lookup_field = 'username'
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs['account_username']
        return (Post.objects
                .select_related('author')
                .filter(author__username=username))
