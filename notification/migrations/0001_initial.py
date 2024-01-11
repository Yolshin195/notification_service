# Generated by Django 5.0.1 on 2024-01-11 12:18

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('timezone', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('message_text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MessageStatusReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MobileOperatorCodeReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TagReference',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.client')),
                ('dispatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.dispatch')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.messagestatusreference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dispatch',
            name='filter_mobile_operator_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.mobileoperatorcodereference'),
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_operator_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.mobileoperatorcodereference'),
        ),
        migrations.AddField(
            model_name='dispatch',
            name='filter_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.tagreference'),
        ),
        migrations.AddField(
            model_name='client',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.tagreference'),
        ),
    ]
