# Generated by Django 3.1.4 on 2020-12-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20201216_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='romanized_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
