# Generated by Django 4.2.2 on 2023-08-23 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.CharField(auto_created=True, default=uuid.UUID('b58e89c9-c3bd-475d-9459-addbb588befd'), max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]