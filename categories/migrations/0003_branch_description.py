# Generated by Django 3.1.4 on 2020-12-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
