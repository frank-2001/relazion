# Generated by Django 5.0.3 on 2024-03-21 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('users', '0002_passions_alter_users_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='id_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receivers', to='users.users'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='id_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to='users.users'),
        ),
    ]
