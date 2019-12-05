from django.contrib import admin

# Register your models here.
from .models import Pet
admin.site.register(Pet)   # tell django to create forms on ui.

