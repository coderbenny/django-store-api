# Generated by Django 5.0.6 on 2024-05-31 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='item_id',
            new_name='item',
        ),
    ]