# Generated by Django 3.2.5 on 2021-09-08 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210907_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='autor',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
