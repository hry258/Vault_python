# Generated by Django 3.1.1 on 2020-10-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201002_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, default='Photo', max_length=30, null=True),
        ),
    ]
