# Generated by Django 3.2.9 on 2021-11-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='likes',
            field=models.IntegerField(default=-1),
        ),
    ]
