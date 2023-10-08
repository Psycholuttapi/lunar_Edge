# Generated by Django 4.2.5 on 2023-10-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="soft_delete",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product_variant",
            name="soft_delete",
            field=models.BooleanField(default=False),
        ),
    ]