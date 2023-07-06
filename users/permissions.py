from rest_framework import permissions

class UserApiPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # denying permission to other users for updating someother users data.
            if request.user.id != view.kwargs['pk'] and request.method != 'GET':
                return False
            return True