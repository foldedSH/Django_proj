# Generated by Django 2.2.5 on 2022-01-26 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20220126_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lender',
            name='object_num',
        ),
    ]