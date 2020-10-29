# Generated by Django 3.1.2 on 2020-10-28 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('made_for', models.CharField(max_length=50)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('description', models.TextField(max_length=3000)),
                ('condition', models.CharField(max_length=50)),
                ('delivery_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='core.brand')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='User_bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Bid',
                'verbose_name_plural': 'User Bids',
            },
        ),
        migrations.CreateModel(
            name='Property_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_name', to='core.category')),
            ],
            options={
                'verbose_name': 'Property Name',
                'verbose_name_plural': 'Property Names',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='core.property_name')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Product_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_stock', models.BinaryField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_property', to='core.product')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_property', to='core.property')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='core.category'),
        ),
    ]