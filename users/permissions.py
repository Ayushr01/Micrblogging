from rest_framework import permissions

class UserApiPermissions(permissions.BasePermission):
    """
    Permissions for users update
    """
    message = " You cannot edit details of other users"
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # denying permission to other users for updating someother users data.
            if str(request.user.id) != view.kwargs['pk'] and request.method != 'GET':
                return False
            return True