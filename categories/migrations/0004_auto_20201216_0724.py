# Generated by Django 3.1.4 on 2020-12-16 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20201215_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]