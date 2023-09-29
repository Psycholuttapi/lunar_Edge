# Generated by Django 4.2 on 2023-09-26 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=25, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=49)),
                ('product_slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('product_description', models.TextField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_management.brand')),
                ('product_catg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category_management.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=30)),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('product_variant_slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('thumbnail_image', models.ImageField(upload_to='products/thumbnail')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attributes', models.ManyToManyField(related_name='attributes', to='product_management.attribute_value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='product_variant',
            constraint=models.UniqueConstraint(condition=models.Q(('model_id__isnull', False)), fields=('product', 'model_id'), name='Unique skuid must be provided'),
        ),
    ]
