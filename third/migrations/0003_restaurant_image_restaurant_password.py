# Generated by Django 4.0.6 on 2022-07-11 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
