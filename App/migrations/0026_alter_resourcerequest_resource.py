# Generated by Django 5.0.6 on 2024-10-17 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_alter_resourcerequest_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcerequest',
            name='resource',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='App.resource'),
        ),
    ]
