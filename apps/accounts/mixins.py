from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

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