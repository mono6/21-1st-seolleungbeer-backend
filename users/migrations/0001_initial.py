# Generated by Django 3.2.4 on 2021-06-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('profile_image', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('mobile', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
