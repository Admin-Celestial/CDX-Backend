# Generated by Django 4.2.6 on 2024-03-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_sources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file_type',
            field=models.FileField(default='pdf', upload_to=''),
        ),
    ]