# Generated by Django 3.2.9 on 2021-12-05 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='updated_at',
        ),
    ]
