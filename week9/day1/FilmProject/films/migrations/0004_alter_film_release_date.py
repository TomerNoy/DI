# Generated by Django 3.2.9 on 2021-11-28 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_film_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
