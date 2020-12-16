from django.contrib import admin

from . import models
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    search_fields = ['name', 'acronym']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(models.Branch, BranchAdmin)
admin.site.register(models.Category,CategoryAdmin)
