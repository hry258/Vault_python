from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.forms import SignUpForm, LoginForm, UploadPhotoForm
from user.models import UserExtended, Photo

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

@login_required(login_url='login')
def upload_photo(request):
    if request.method == "POST":
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user_extended = UserExtended.objects.get(username=user.id)
            photo = form.cleaned_data['photo']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            photo_obj = Photo(photo=photo, title=title, description=description, photo_id=user_extended, date=date)
            photo_obj.save()
            msj = "Picture uploaded!"
            return render(request, 'upload_photo.html', {"form": form, "upload_message": msj})
    else:
        form = UploadPhotoForm()
    return render(request, 'upload_photo.html', {"form": form})

@login_required(login_url='login')
def view_photos(request):
    user = User.objects.get(username=request.user.username)
    user_extended = UserExtended.objects.get(username=user.id)
    return render(request, 'photos.html', {"user_extended": user_extended})