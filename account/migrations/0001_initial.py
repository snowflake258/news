# Generated by Django 3.1.1 on 2020-09-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Электронная почта')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор?')),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
    ]
