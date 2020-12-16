# Generated by Django 3.1.4 on 2020-12-16 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20201216_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('acronym', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='songs.branch'),
        ),
    ]