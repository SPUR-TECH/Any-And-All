# Generated by Django 3.2 on 2022-09-27 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='updated_on',
        ),
    ]