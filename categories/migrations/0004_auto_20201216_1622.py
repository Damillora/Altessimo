# Generated by Django 3.1.4 on 2020-12-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_branch_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='acronym',
            field=models.CharField(max_length=20),
        ),
    ]
