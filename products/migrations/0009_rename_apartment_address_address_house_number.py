# Generated by Django 3.2 on 2022-08-13 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_address_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='apartment_address',
            new_name='house_number',
        ),
    ]
