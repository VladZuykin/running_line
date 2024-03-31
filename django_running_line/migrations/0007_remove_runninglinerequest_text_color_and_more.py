# Generated by Django 5.0.3 on 2024-03-30 22:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_running_line', '0006_runninglinerequest_bg_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runninglinerequest',
            name='text_color',
        ),
        migrations.AlterField(
            model_name='runninglinerequest',
            name='bg_color',
            field=models.CharField(default='#000000', max_length=7, validators=[django.core.validators.RegexValidator('^#[0-9A-Fa-f]{6}$', message='Color must be in hex format.')]),
        ),
    ]
