# Generated by Django 4.0.7 on 2023-02-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trust_scoring', '0002_contractfeatures_web3js_uses'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractfeatures',
            name='avg_gas_price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
