# Generated by Django 5.1.2 on 2024-10-19 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0029_resourcerequest_resource"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resourcerequest",
            name="is_approved",
        ),
        migrations.RemoveField(
            model_name="resourcerequest",
            name="resource",
        ),
    ]
