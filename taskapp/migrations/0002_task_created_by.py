# Generated by Django 5.0.1 on 2024-02-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
