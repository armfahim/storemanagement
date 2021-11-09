# Generated by Django 3.2.9 on 2021-11-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemanagement', '0002_remove_product_sellingprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sellingPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
