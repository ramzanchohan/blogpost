# Generated by Django 4.2.3 on 2023-07-30 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0011_alter_blogpost_pub_date_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
