# Generated by Django 3.0.5 on 2020-05-12 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pal', '0010_users_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
    ]
