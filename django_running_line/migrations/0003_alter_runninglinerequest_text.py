# Generated by Django 5.0.3 on 2024-03-30 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_running_line', '0002_alter_runninglinerequest_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runninglinerequest',
            name='text',
            field=models.TextField(max_length=128),
        ),
    ]
