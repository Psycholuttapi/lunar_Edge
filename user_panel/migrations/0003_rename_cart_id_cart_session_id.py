# Generated by Django 4.2 on 2023-09-29 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0002_alter_cart_total_price_alter_cart_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='session_id',
        ),
    ]