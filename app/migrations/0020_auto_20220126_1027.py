# Generated by Django 2.2.5 on 2022-01-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_borrower_borrower_chatting_lender_lender_chatting_object_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]