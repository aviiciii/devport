# Generated by Django 4.1.3 on 2022-11-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(default='user', max_length=50)),
                ('about', models.TextField(blank=True, max_length=500)),
                ('college', models.CharField(blank=True, max_length=100)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('grade', models.CharField(blank=True, max_length=100)),
                ('graduation_year', models.CharField(blank=True, max_length=100)),
                ('contact_email', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('github', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
