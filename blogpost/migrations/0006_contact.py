# Generated by Django 4.2.3 on 2023-07-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0005_alter_blogpost_author_alter_blogpost_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
            ],
        ),
    ]
