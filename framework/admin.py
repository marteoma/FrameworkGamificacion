from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin


class Configurations(models.Model):
    p1 = models.CharField(default='75%', max_length=5)


admin.site.register(Configurations)
# admin.site.register(get_percentage)
