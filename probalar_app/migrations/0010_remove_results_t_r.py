# Generated by Django 4.0.3 on 2022-03-23 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probalar_app', '0009_alter_results_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='t_r',
        ),
    ]