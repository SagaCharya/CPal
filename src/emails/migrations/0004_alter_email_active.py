# Generated by Django 5.1.7 on 2025-05-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0003_email_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
