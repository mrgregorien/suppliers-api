# Generated by Django 4.1.3 on 2022-12-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_rename_suppliersmodels_suppliersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='suppliersmodel',
            name='ProductUrlReference',
            field=models.URLField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='suppliersmodel',
            name='SubCategory',
            field=models.CharField(blank=True, default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='Category',
            field=models.CharField(choices=[('Appliances', 'Appliances'), ('Apps & Games', 'Apps & Games'), ('Arts Crafts & Sewing', 'Arts Crafts & Sewing'), ('Automotive Parts & Accessories', 'Automotive Parts & Accessories'), ('Baby', 'Baby'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('CDs & Vinyl', 'CDs & Vinyl'), ('Cell Phones & Accessories', 'Cell Phones & Accessories'), ('Clothing Shoes & Jewelry', 'Clothing Shoes & Jewelry'), ('Collectibles & Fine Art', 'Collectibles & Fine Art'), ('Computers & Accessories', 'Computers & Accessories'), ('Credit and Payment Cards', 'Credit and Payment Cards'), ('Digital Educational Resources', 'Digital Educational Resources'), ('Digital Music', 'Digital Music'), ('Electronics', 'Electronics'), ('Garden & Outdoor', 'Garden & Outdoor'), ('Gift Cards', 'Gift Cards'), ('Grocery & Gourmet Food', 'Grocery & Gourmet Food'), ('Handmade', 'Handmade'), ('Health Household & Baby Care', 'Health Household & Baby Care'), ('Home & Business Services', 'Home & Business Services'), ('Home & Kitchen', 'Home & Kitchen'), ('Industrial & Scientific', 'Industrial & Scientific'), ('Luggage & Travel Gear', 'Luggage & Travel Gear'), ('Luxury Stores', 'Luxury Stores'), ('Magazine Subscriptions', 'Magazine Subscriptions'), ('Movies & TV', 'Movies & TV'), ('Musical Instruments', 'Musical Instruments'), ('Office Products', 'Office Products'), ('Online Learning', 'Online Learning'), ('Pet Supplies', 'Pet Supplies'), ('Premium Beauty', 'Premium Beauty'), ('Smart Home', 'Smart Home'), ('Software', 'Software'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Subscription Boxes', 'Subscription Boxes'), ('Tools & Home Improvement', 'Tools & Home Improvement'), ('Toys & Games', 'Toys & Games')], default='Category', max_length=80),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='ContactName',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='ContactTitle',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='Email',
            field=models.EmailField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='Phone',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='suppliersmodel',
            name='PostalCode',
            field=models.IntegerField(default=''),
        ),
    ]
