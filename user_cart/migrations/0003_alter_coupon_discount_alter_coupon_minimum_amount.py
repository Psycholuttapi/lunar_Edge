# Generated by Django 4.2.5 on 2023-10-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_cart", "0002_alter_coupon_expiration_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coupon",
            name="discount",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name="coupon",
            name="minimum_amount",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]