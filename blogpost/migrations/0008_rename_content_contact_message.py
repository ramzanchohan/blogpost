# Generated by Django 4.2.3 on 2023-07-29 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0007_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='message',
        ),
    ]
