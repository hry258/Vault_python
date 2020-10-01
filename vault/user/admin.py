from django.contrib import admin
from user.models import Photo, UserExtended

# Register your models here.

class PhotoAdminInLine(admin.TabularInline):
    model = Photo

class UserExtendedAdmin(admin.ModelAdmin):
    inlines = (PhotoAdminInLine, )
    list_display = ['username', 'first_name', 'last_name', 'email', 'picture']

admin.site.register(UserExtended, UserExtendedAdmin)