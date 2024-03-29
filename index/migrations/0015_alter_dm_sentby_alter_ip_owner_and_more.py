# Generated by Django 4.1.5 on 2023-03-27 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0014_alter_ip_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dm',
            name='sentBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.ip'),
        ),
        migrations.AlterField(
            model_name='ip',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='blocked_ips',
            field=models.ManyToManyField(blank=True, to='index.ip'),
        ),
    ]
