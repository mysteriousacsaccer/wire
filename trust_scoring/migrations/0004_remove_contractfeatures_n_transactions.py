# Generated by Django 4.0.7 on 2023-03-07 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trust_scoring', '0003_contractfeatures_avg_gas_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractfeatures',
            name='n_transactions',
        ),
    ]
