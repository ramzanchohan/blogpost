# Generated by Django 4.2.3 on 2023-07-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='null', max_length=200)),
                ('content', models.TextField(default='null')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
