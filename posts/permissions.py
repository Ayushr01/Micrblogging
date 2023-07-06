from rest_framework import permissions
from .models import Post

class PostApiPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # denying permission to other users for updating someother users Post.
            post_creator = Post.objects.only('id').get(id=view.kwargs['pk'])
            print(request.user.id)
            print(post_creator.id)
            print(request.method)
            if request.user.id != post_creator.id and request.method == 'PATCH':
                return False
            return True