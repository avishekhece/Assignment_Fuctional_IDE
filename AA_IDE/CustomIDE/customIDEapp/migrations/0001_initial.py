# Generated by Django 5.0.2 on 2024-02-22 22:58

import customIDEapp.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('accepted_input_type', customIDEapp.models.PythonDataField()),
                ('accepted_output_type', customIDEapp.models.PythonDataField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('response_message', models.TextField()),
                ('output_value', models.TextField(blank=True, null=True)),
                ('success_status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executions', to='customIDEapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('input_data', models.TextField()),
                ('expected_output', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('executions', models.ManyToManyField(related_name='test_cases', to='customIDEapp.execution')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customIDEapp.question')),
            ],
        ),
    ]
