# Generated by Django 2.2 on 2020-02-18 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_auto_20200218_0536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Sold Product', 'verbose_name_plural': 'Sold Products'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='barcode',
        ),
    ]