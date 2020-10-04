from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.forms import SignUpForm, LoginForm, UploadPhotoForm
from user.models import UserExtended, Photo

def get_user_extended(request):
    user = User.objects.get(username=request.user.username)
    user_extended = UserExtended.objects.get(username=user.id)
    return user_extended

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
    user_extended = get_user_extended(request)
    return render(request, 'home.html', {"user_extended": user_extended})

@login_required(login_url='login')
def upload_photo(request):
    if request.method == "POST":
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user_extended = get_user_extended(request)
            photo = form.cleaned_data['photo']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            photo_obj = Photo(photo=photo, title=title, description=description, photo_id=user_extended)
            photo_obj.save()
            msj = "Picture uploaded!"
            return render(request, 'upload_photo.html', {"form": form, "upload_message": msj})
    else:
        form = UploadPhotoForm()
    return render(request, 'upload_photo.html', {"form": form})

@login_required(login_url='login')
def view_photos(request):
    user_extended = get_user_extended(request)
    try:
        user_photos = Photo.objects.filter(photo_id=user_extended)
        return render(request, 'photos.html', {"user_photos": user_photos})
    except Exception as error:
        return render(request, 'photos.html', {"error": error})

@login_required(login_url='login')
def profile(request):
    user_extended = get_user_extended(request)
    return render(request, 'profile.html', {'user_extended': user_extended})

# @login_required(login_url='login')
# def edit_profile(request):
#     if request.method == 'POST':
#         form =
#         if form.is_valid():
#             user_extended = get_user_extended(request)
#             return render(request, 'edit_profile.html', {'user_extended': user_extended})
#     else:
#         form =
#     return render(request, 'edit_profile.html', {'form': form})