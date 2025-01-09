# Generated by Django 5.1.4 on 2025-01-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(unique=True)),
                ('assign_to', models.CharField()),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
