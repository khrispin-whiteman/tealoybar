# Generated by Django 2.2 on 2020-02-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_auto_20200209_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditor',
            name='addamount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Add New Item Price'),
        ),
    ]
