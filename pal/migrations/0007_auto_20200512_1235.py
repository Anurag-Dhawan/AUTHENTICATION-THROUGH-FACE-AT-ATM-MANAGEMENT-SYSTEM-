# Generated by Django 3.0.5 on 2020-05-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pal', '0006_users_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='DOB',
            field=models.DateField(default='2006-10-25'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='add',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='mail',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
