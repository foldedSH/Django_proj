# Generated by Django 2.2.5 on 2022-01-26 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220126_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Borrower',
        ),
        migrations.DeleteModel(
            name='Borrower_Chatting',
        ),
        migrations.DeleteModel(
            name='Lender',
        ),
        migrations.DeleteModel(
            name='Lender_Chatting',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]