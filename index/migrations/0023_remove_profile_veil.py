# Generated by Django 4.0.6 on 2023-12-01 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_profile_dp_alter_profile_bio_alter_profile_veil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='veil',
        ),
    ]
