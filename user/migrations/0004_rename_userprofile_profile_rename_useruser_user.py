# Generated by Django 4.0.4 on 2022-05-05 15:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_userprofile_profile_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.RenameModel(
            old_name='UserUser',
            new_name='User',
        ),
    ]
