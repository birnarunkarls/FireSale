# Generated by Django 4.0.4 on 2022-05-06 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0002_alter_bid_buyer_id_alter_item_seller_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='seller_id',
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(default='', max_length=9999),
        ),
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(default='', max_length=9999),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='highest_bid',
            field=models.CharField(default='', max_length=9999),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='IMG', max_length=9999),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=9999),
        ),
    ]
