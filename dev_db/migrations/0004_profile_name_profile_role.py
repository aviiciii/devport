# Generated by Django 4.1.3 on 2022-11-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_db', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
