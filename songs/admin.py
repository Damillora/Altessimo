from django.contrib import admin

from . import models


class SongAdmin(admin.ModelAdmin):
    search_fields = ['romanized_title','title']

class OutsideSongAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(models.Song, SongAdmin)
admin.site.register(models.OutsideSong, OutsideSongAdmin)
