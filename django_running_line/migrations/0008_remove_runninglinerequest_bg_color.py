# Generated by Django 5.0.3 on 2024-03-30 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_running_line', '0007_remove_runninglinerequest_text_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runninglinerequest',
            name='bg_color',
        ),
    ]
