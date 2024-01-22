# Generated by Django 4.1.13 on 2024-01-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_password_user_desiredservice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotSteps',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('user', models.BooleanField(default=False, null=True)),
                ('trigger', models.CharField(max_length=255, null=True)),
                ('validator', models.BooleanField(default=False, null=True)),
                ('options', models.JSONField(blank=True, null=True)),
                ('end', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]