# Generated by Django 5.0.2 on 2024-02-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customIDEapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='accepted_input_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='accepted_output_type',
        ),
    ]
