from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import UserRegisterForm




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully, Please Login')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {"form":form})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, f'Please Login to Access this page')
        return redirect('login')
    else:
        return render(request, 'users/profile.html')