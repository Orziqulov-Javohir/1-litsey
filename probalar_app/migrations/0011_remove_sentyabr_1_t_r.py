# Generated by Django 4.0.3 on 2022-03-23 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probalar_app', '0010_remove_results_t_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentyabr_1',
            name='t_r',
        ),
    ]
