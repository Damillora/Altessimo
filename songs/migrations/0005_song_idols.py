# Generated by Django 3.2.5 on 2021-07-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_idol_voiceactor'),
        ('songs', '0004_auto_20201217_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='idols',
            field=models.ManyToManyField(blank=True, related_name='idol_songs', to='artists.Idol'),
        ),
    ]
