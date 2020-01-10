from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        # print("inside if")
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            print("inside valid if")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! ')
            return redirect('login')
    else:
        # print("inside else")
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required()
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        # print (u_form.data,p_form)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated! ')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # print(u_form)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    print(context)
    return render(request, 'user/profile.html', context)

