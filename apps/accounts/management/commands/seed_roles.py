from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Seed initial roles and permissions"
    
    def handle(self, *args, **kwargs):
        
        user_group, _ = Group.objects.get_or_create(name="User")
        staff_group, _ = Group.objects.get_or_create(name="Staff")
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        
        view_user_permission = Permission.objects.get(codename="view_user")
        change_user_permission = Permission.objects.get(codename="change_user")
        
        staff_group.permissions.add(view_user_permission,)
        admin_group.permissions.add(view_user_permission,change_user_permission,)
        
        self.stdout.write(self.style.SUCCESS("Roles and permissions seeded successfully."))
        
        
        self.stdout.write(self.style.SUCCESS("Groups created successfully."))
        