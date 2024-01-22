# Generated by Django 5.0.1 on 2024-01-22 08:27

import notification.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_dispatch_timezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageIdTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='message_id',
            field=models.IntegerField(default=notification.models.MessageIdTable.get_next_id, editable=False, unique=True),
        ),
    ]
