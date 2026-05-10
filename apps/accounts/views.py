from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    form= LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials")
                
        return render(request, "accounts/login.html", {"form": forms})
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("login")
            
            








#from django.views.generic import TemplateView

'''
class IndexView(TemplateView):
    template_name = "accounts/index.html"
'''
