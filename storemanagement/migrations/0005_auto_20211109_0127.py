# Generated by Django 3.2.9 on 2021-11-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storemanagement', '0004_salesinvoice_salesinvoicedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoicedetails',
            name='invoiceNumber',
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='invoiceDate',
            field=models.CharField(max_length=100),
        ),
    ]
