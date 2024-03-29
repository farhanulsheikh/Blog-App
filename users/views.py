from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import UserRegisterForm ,ProfileUpdateForm, UserUpdateForm





def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully, Please Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {"form":form})


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, f'Please Login to Access this page')
        return redirect('login')
    else:
        if request.method == "POST":
            u_form = UserUpdateForm(request.POST,instance =request.user)
            p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Account Updated')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance =request.user)
            p_form = ProfileUpdateForm(instance = request.user.profile)

            context = {
                'u_form':u_form,
                'p_form':p_form
            }
            return render(request, 'users/profile.html',context)
