# Generated by Django 5.0.6 on 2024-07-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
