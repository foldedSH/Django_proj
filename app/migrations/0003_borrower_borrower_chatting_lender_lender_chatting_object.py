# Generated by Django 2.2.5 on 2022-01-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220124_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('b_posting_index', models.IntegerField(primary_key=True, serialize=False)),
                ('borrower_index', models.IntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrower_Chatting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_index', models.IntegerField()),
                ('object_num', models.IntegerField()),
                ('date', models.DateField()),
                ('chatting', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('l_posting_index', models.IntegerField(primary_key=True, serialize=False)),
                ('lender_index', models.IntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255, null=True)),
                ('rentalfee', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('object_num', models.IntegerField()),
                ('pic', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lender_Chatting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_index', models.IntegerField()),
                ('object_num', models.IntegerField()),
                ('date', models.DateField()),
                ('chatting', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('object_index', models.IntegerField(primary_key=True, serialize=False)),
                ('object_name', models.CharField(max_length=255, null=True)),
                ('borrower_index', models.IntegerField()),
                ('posting_index', models.IntegerField()),
                ('rental_fee', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('lender_index', models.IntegerField()),
            ],
        ),
    ]
