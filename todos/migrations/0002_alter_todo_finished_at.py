# Generated by Django 5.1 on 2024-08-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
