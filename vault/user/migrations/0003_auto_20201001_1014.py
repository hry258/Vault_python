# Generated by Django 3.1.1 on 2020-10-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201001_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
