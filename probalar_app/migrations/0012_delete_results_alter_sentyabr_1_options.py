# Generated by Django 4.0.3 on 2022-03-23 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('probalar_app', '0011_remove_sentyabr_1_t_r'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Results',
        ),
        migrations.AlterModelOptions(
            name='sentyabr_1',
            options={'ordering': ['-Jami'], 'verbose_name': '1 -kurslar Sentyabr', 'verbose_name_plural': '1 -kurslar Sentyabr'},
        ),
    ]