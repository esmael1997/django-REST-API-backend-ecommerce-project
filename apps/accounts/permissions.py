from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Only admin/staff/superuser
    """

    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and (
                user.is_staff or user.is_superuser or
                user.groups.filter(name="admin").exists()
            )
        )


class IsCustomerUser(BasePermission):
    """
    Only normal customers
    """

    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and
            user.groups.filter(name="customer").exists()
        )
        