# Generated by Django 2.0.7 on 2018-08-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_auto_20180807_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedbinfo',
            name='created',
            field=models.DateTimeField(),
        ),
    ]