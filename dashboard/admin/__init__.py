from django.contrib import admin
from django.contrib.auth.models import User
from reversion.admin import VersionAdmin
from application import models
from dashboard.admin.UserAdmin import UserProfileAdmin

admin.site.register(models.UserProfile, UserProfileAdmin)