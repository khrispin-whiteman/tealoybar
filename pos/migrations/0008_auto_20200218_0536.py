# Generated by Django 2.2 on 2020-02-18 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_creditor_addamount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditor',
            options={'verbose_name': 'Ba Nkongole', 'verbose_name_plural': 'Ba Nkongole'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Sales', 'verbose_name_plural': 'Sales'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Sold Item', 'verbose_name_plural': 'Sold Items'},
        ),
    ]