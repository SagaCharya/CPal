# Generated by Django 5.1.7 on 2025-03-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_lesson_public_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='public_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='public_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
