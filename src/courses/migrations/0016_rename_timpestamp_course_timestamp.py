# Generated by Django 5.1.7 on 2025-03-21 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_rename_timpestamp_lesson_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='timpestamp',
            new_name='timestamp',
        ),
    ]
