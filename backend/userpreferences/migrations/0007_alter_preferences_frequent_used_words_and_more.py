# Generated by Django 5.0.3 on 2024-03-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0006_alter_preferences_frequent_used_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='frequent_used_words',
            field=models.JSONField(default='{}'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='lockedKeys',
            field=models.JSONField(default='[]'),
        ),
    ]
