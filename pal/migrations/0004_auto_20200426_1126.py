# Generated by Django 3.0.5 on 2020-04-26 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pal', '0003_users_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pal.users')),
            ],
        ),
    ]
