# Generated by Django 4.1.13 on 2023-12-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.CharField(default='b8d79729-c2fb-4777-9863-1a15f47d6431', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.CharField(default='8a40266a-8163-4d5a-b71b-d0f2d338a125', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(default='bba1f6f2-3201-4bbd-b204-e34f09f1ef67', editable=False, max_length=100)),
                ('ingredient', models.CharField(default='9b589556-ad64-4b68-bec7-6a49c32d9711', editable=False, max_length=100)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default='fb99877b-56a1-446f-bd62-2d2c8c2fd8f3', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('item', models.CharField(default='195ef38b-0b85-4fed-bcdf-e8926ceb3b0a', editable=False, max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(default='e2076ff0-7c96-4dff-8050-1bce88075f04', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('order', models.CharField(default='8a05bcca-43fc-44f4-aa22-8f7695864ecc', editable=False, max_length=100)),
                ('method', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
