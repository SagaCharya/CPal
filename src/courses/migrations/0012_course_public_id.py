# Generated by Django 5.1.7 on 2025-03-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_alter_lesson_options_course_timpestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='public_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
