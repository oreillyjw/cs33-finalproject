# Generated by Django 2.0.7 on 2018-08-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedbinfo',
            name='type',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
