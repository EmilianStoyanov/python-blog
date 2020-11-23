from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})