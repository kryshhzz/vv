# Generated by Django 4.1.7 on 2023-04-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_profile_is_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='dm',
            name='viewOnce',
            field=models.BooleanField(default=False),
        ),
    ]
