from django.contrib import admin
from django import forms

from .models import Branch, Category
# Register your models here.

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'tm-textfield'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'tm-textfield'
    
class BranchAdmin(admin.ModelAdmin):
    form = BranchForm
    search_fields = ['name', 'acronym']

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.6.2/tinymce.min.js',
            'tinymce-init.js'
        )

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    search_fields = ['name']

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.6.2/tinymce.min.js',
            'tinymce-init.js'
        )

admin.site.register(Branch, BranchAdmin)
admin.site.register(Category,CategoryAdmin)
