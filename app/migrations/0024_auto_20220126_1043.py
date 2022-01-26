# Generated by Django 2.2.5 on 2022-01-26 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20220126_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='borrower_index',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lender',
            name='lender_index',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.User'),
            preserve_default=False,
        ),
    ]