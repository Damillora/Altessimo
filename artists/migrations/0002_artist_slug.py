# Generated by Django 3.1.4 on 2020-12-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
