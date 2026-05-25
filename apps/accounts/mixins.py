from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class StaffRequiredMixin:
    allowed_roles = ["staff", "admin"]

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user.groups.filter(name__in=self.allowed_roles).exists():
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

def create_roles():
    roles = ["customer", "staff", "admin"]

    for role in roles:
        Group.objects.get_or_create(name=role)

'''
class StaffRequiredMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        
        if (request.user.is_authenticated and request.user.groups.filter(name="Staff").exists()):
            
            return super().dispatch(request, *args, **kwargs)
        
        raise PermissionDenied
    
class AdminRequiredMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        
        if(request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()):
            
            return super().dispatch(request, *args, **kwargs)
        
        raise PermissionDenied
        
'''
    
def assign_role(user, role_name: str):
    group = Group.objects.get(name=role_name)
    user.groups.add(group)
    
def has_role(user, roles: list[str]) -> bool:
    return user.groups.filter(name__in=roles).exists()

class AdminRequiredMixin:
    allowed_roles = ["admin"]

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user.groups.filter(name="admin").exists():
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
    
class OwnerRequiredMixin:

    def dispatch(self, request, *args, **kwargs):

        obj = self.get_object()

        if obj.user != request.user and not request.user.groups.filter(name="admin").exists():
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)