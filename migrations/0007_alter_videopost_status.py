# Generated by Django 5.0.6 on 2024-06-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_videopost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='status',
            field=models.CharField(choices=[(-1, 'decline'), (0, 'in process'), (1, 'published')], max_length=2),
        ),
    ]
