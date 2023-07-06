from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from posts.permissions import PostApiPermissions

from posts.serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostApiPermissions,)
    http_method_names = ['get', 'post', 'patch']
    lookup_field = "pk"
