# Generated by Django 2.2.5 on 2022-01-26 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20220126_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower_chatting',
            name='posting_index',
            field=models.ForeignKey(db_column='b_posting_index', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Borrower'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lender_chatting',
            name='posting_index',
            field=models.ForeignKey(db_column='l_posting_index', default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Lender'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='borrower',
            name='body',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='borrower_chatting',
            name='chatting',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lender',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='lender_chatting',
            name='chatting',
            field=models.TextField(),
        ),
    ]
