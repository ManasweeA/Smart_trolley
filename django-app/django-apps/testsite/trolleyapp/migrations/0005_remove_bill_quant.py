# Generated by Django 3.0.6 on 2020-05-27 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trolleyapp', '0004_bill_quant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='quant',
        ),
    ]
