# Generated by Django 4.0.4 on 2022-05-09 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_itemimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemImages',
            new_name='Images',
        ),
    ]
