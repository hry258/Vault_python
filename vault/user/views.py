from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.forms import SignUpForm, LoginForm
from user.models import UserExtended

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_extended = UserExtended(username=user, email=form.cleaned_data['email'])
            user_extended.save()
            return render(request, 'home.html', {'user_extended': user_extended})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def home(request):
    user = User.objects.get(username=request.user.username)
    user_extended = UserExtended.objects.get(username=user.id)
    return render(request, 'home.html', {"user_extended": user_extended})
