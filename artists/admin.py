from django.contrib import admin
from . import models
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['romanized_name','name']

admin.site.register(models.Artist, ArtistAdmin)
