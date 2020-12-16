# Generated by Django 3.1.4 on 2020-12-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outsidesong',
            name='romanized_title',
        ),
        migrations.AddField(
            model_name='outsidesong',
            name='artist',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='outsidesong',
            name='origin',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='outsidesong',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='outsidesong',
            name='url',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]