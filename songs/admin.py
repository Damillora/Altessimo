from django import forms
from django.contrib import admin

from .models import Song, OutsideSong
from artists.models import Artist
from idols.models import Idol


class SongForm(forms.ModelForm):
    lyricist_str = forms.CharField(label='Lyricists', required=False)
    composer_str = forms.CharField(label='Composers', required=False)
    arranger_str = forms.CharField(label='Arrangers', required=False)
    idols_str = forms.CharField(label='Idols', required=False)

    class Meta:
        model = Song
        fields = [
            'branch',
            'title',
            'romanized_title',
            'lyricist_str',
            'composer_str',
            'arranger_str',
            'idols_str',
            'impression',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['impression'].widget.attrs['class'] = 'tm-textfield'
        instance = kwargs.get("instance")
        if instance:
            self.fields['lyricist_str'].initial = ', '.join(
                x.romanized_name for x in instance.lyricist.all())
            self.fields['composer_str'].initial = ', '.join(
                x.romanized_name for x in instance.composer.all())
            self.fields['arranger_str'].initial = ', '.join(
                x.romanized_name for x in instance.arranger.all())
            self.fields['idols_str'].initial = ', '.join(
                x.romanized_name for x in instance.idols.all())


class SongAdmin(admin.ModelAdmin):
    form = SongForm
    search_fields = ['romanized_title', 'title']

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/tinymce/5.6.2/tinymce.min.js',
            'tinymce-init.js'
        )

    def save_model(self, request, obj, form, change):
        lyricist_str = form.cleaned_data.get('lyricist_str')
        composer_str = form.cleaned_data.get('composer_str')
        arranger_str = form.cleaned_data.get('arranger_str')
        idols_str = form.cleaned_data.get('idols_str')
        lyricist = Artist.objects.comma_to_qs(lyricist_str)
        composer = Artist.objects.comma_to_qs(composer_str)
        arranger = Artist.objects.comma_to_qs(arranger_str)
        idols = Idol.objects.comma_to_qs(idols_str)
        if not obj.id:
            obj.save()
        obj.lyricist.clear()
        obj.lyricist.add(*lyricist)
        obj.composer.clear()
        obj.composer.add(*composer)
        obj.arranger.clear()
        obj.arranger.add(*arranger)
        obj.idols.clear()
        obj.idols.add(*idols)
        obj.save()


class OutsideSongAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Song, SongAdmin)
admin.site.register(OutsideSong, OutsideSongAdmin)
