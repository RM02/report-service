# Generated by Django 4.2.2 on 2023-08-23 15:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.CharField(default=uuid.UUID('38108be8-6995-42c2-a4b4-6ed1ed803de0'), max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
