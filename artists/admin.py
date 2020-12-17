from django.contrib import admin
from django import forms

from .models import Artist
from categories.models import Category

# Register your models here.
class ArtistForm(forms.ModelForm):
    categories_str = forms.CharField(label='Category', required=False)
    aliases_str = forms.CharField(label='Aliases', required=False)
    class Meta:
        model = Artist
        fields = [
            'name',
            'romanized_name',
            'slug',
            'categories_str',
            'aliases_str',
            'about_artist',
            'about_music',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['about_artist'].widget.attrs['class'] = 'tm-textfield'
        self.fields['about_music'].widget.attrs['class'] = 'tm-textfield'
        instance = kwargs.get("instance")
        if instance:
            self.fields['categories_str'].initial = ", ".join(x.name for x in instance.category.all() )
            self.fields['aliases_str'].initial = ", ".join(x.romanized_name for x in instance.aliases.all() )

class ArtistAdmin(admin.ModelAdmin):
    form = ArtistForm
    search_fields = ['romanized_name','name']

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.6.2/tinymce.min.js',
            'tinymce-init.js'
        )
    def save_model(self, request, obj, form, change):
        categories_str = form.cleaned_data.get('categories_str')
        categories = Category.objects.comma_to_qs(categories_str)
        aliases_str = form.cleaned_data.get('aliases_str')
        aliases = Artist.objects.comma_to_qs(aliases_str)
        if not obj.id:
            obj.save()
        obj.category.clear()
        obj.category.add(*categories)
        obj.aliases.clear()
        obj.aliases.add(*aliases)
        obj.save()

admin.site.register(Artist, ArtistAdmin)
