# Generated by Django 5.0.6 on 2024-05-15 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corpershub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonflex',
            name='corper_name',
        ),
    ]
