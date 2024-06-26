# Generated by Django 4.2.6 on 2024-03-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartqueryHistory',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('response', models.CharField(max_length=10000)),
                ('U_ID', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField()),
                ('status', models.CharField(choices=[('0', 'Dis-liked'), (None, 'Not Responded'), ('1', 'Liked')], default=None, max_length=1, null=True)),
            ],
            options={
                'db_table': 'smartquery_chathistory',
                'managed': False,
            },
        ),
    ]
