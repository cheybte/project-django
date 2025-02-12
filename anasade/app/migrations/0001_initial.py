# Generated by Django 5.1.4 on 2025-01-13 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Moughataa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('label', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('unit_measure', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('label', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=252)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('moughataa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.moughataa')),
            ],
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('gps_lat', models.FloatField()),
                ('gps_lon', models.FloatField()),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commune')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('cart_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('point_of_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pointofsale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producttype'),
        ),
        migrations.AddField(
            model_name='moughataa',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wilaya'),
        ),
    ]
