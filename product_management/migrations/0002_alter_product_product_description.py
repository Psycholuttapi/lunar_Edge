# Generated by Django 4.2.5 on 2023-10-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_description",
            field=models.TextField(max_length=5000),
        ),
    ]