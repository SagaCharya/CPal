# Generated by Django 5.1.7 on 2025-05-04 06:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_alter_email_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverificationevent',
            name='token',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]
