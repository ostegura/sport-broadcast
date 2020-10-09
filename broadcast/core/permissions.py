from rest_framework import permissions

# from django.contrib.auth.models import Group


# def _is_in_group(user, group_name):
#     """
#     Takes a user and a group name, and returns `True` if the user is in that group.
#     """
#     try:
#         return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
#     except Group.DoesNotExist:
#         return None


# def _has_group_permission(user, required_groups):
#     return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsOwnerOrReadOnly(permissions.BasePermission):

    # this is custom permission to only allow owners of an
    # object to edit it

    def has_object_permission(self, request, view, obj):
        # read perm's are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # write perm's are only allowed to the owner of the comment
        return obj.owner == request.user
