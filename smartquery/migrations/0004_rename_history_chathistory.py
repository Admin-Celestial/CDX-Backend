# Generated by Django 4.2.6 on 2024-03-07 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartquery', '0003_history_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='ChatHistory',
        ),
    ]