# Generated by Django 2.2.6 on 2020-05-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trolleyapp', '0005_remove_bill_quant'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='pid',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
