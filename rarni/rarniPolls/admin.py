from django.contrib import admin
from .models import User, Email

admin.site.register(User) #registers the User Class under the admin panel
admin.site.register(Email)

