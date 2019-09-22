from django.contrib import admin
# from django.contrib.auth.models import User
# from reversion.admin import VersionAdmin
from application import models
from dashboard.admin.UserAdmin import UserProfileAdmin
from dashboard.admin.LCAdmin import LCAdmin
from dashboard.admin.BILAdmin import BILAdmin

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.LC, LCAdmin)
admin.site.register(models.BIL, BILAdmin)
