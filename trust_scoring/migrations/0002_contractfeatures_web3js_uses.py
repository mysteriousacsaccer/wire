# Generated by Django 4.0.7 on 2023-02-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trust_scoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractfeatures',
            name='web3js_uses',
            field=models.JSONField(default=None, null=True),
        ),
    ]
