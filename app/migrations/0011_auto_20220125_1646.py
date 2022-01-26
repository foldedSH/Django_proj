# Generated by Django 2.2.5 on 2022-01-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220125_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='b_posting_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='borrower_chatting',
            name='b_chatting_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lender',
            name='l_posting_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lender_chatting',
            name='l_chatting_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='object',
            name='object_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
