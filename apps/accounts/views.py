from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def login_view(request):

    #form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")

            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(
                    request,
                    "Login successful"
                )

                return redirect("home")

            else:

                messages.error(
                    request,
                    "Invalid credentials"
                )

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("login")
            

def register_view(request):
    form = RegisterForm(request.Post or None)
    
    if request.method == 'POST':
        
        #form = RegisterForm(request.POST)
        
        if form.is_valid():
            
            user = form.save()
            
            login(request, user)
            
            messages.success(request,'Account created successfully')
            
            return redirect('/')
    #else:
        #form = RegisterForm()
        
    #context = {'form': form}
    
    return render(request,'accounts/register.html', {'form': form})        
            
class IndexView(TemplateView):
    template_name = "accounts/index.html"
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
    
#@login_required
#def profile_view(request):
    #return render(request, "accounts/profile.html")

