# Generated by Django 5.0.3 on 2024-05-26 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_passions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sender', models.IntegerField()),
                ('id_receiver', models.IntegerField()),
                ('message', models.TextField()),
                ('creation_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]