# Generated by Django 2.0.7 on 2018-08-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20180807_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
