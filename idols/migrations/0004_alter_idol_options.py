# Generated by Django 3.2.5 on 2021-07-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idols', '0003_auto_20210709_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idol',
            options={'ordering': ['romanized_name', 'name']},
        ),
    ]