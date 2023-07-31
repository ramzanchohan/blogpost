# Generated by Django 4.2.3 on 2023-07-29 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0004_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='author', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.date(2023, 7, 29)),
        ),
    ]