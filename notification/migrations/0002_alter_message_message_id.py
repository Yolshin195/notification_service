# Generated by Django 5.0.1 on 2024-01-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notification", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="message_id",
            field=models.IntegerField(editable=False, unique=True),
        ),
    ]
