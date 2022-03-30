# Generated by Django 4.0.3 on 2022-03-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probalar_app', '0007_alter_results_jami'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprel_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Aprel',
                'verbose_name_plural': '1-kurslar Aprel',
            },
        ),
        migrations.CreateModel(
            name='Dekabr_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Dekabr',
                'verbose_name_plural': '1-kurslar Dekabr ',
            },
        ),
        migrations.CreateModel(
            name='Fevral_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Fevral',
                'verbose_name_plural': '1-kurslar Fevral',
            },
        ),
        migrations.CreateModel(
            name='Mart_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Mart',
                'verbose_name_plural': '1-kurslar Mart',
            },
        ),
        migrations.CreateModel(
            name='May_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar May',
                'verbose_name_plural': '1-kurslar May',
            },
        ),
        migrations.CreateModel(
            name='Noyabr_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Noyabr',
                'verbose_name_plural': '1-kurslar Noyabr ',
            },
        ),
        migrations.CreateModel(
            name='Oktyabr_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Oktyabr',
                'verbose_name_plural': '1-kurslar Oktyabr ',
            },
        ),
        migrations.CreateModel(
            name='Sentyabr_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Sentyabr',
                'verbose_name_plural': '1-kurslar Sentyabr ',
            },
        ),
        migrations.CreateModel(
            name='Yanvar_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_r', models.IntegerField(null=True)),
                ('F_I_SH', models.CharField(max_length=255, null=True)),
                ('Guruh', models.CharField(max_length=255, null=True)),
                ('Ona_tili', models.IntegerField(default=0, null=True)),
                ('Matem', models.IntegerField(default=0, null=True)),
                ('Tarix', models.IntegerField(default=0, null=True)),
                ('blok_1', models.IntegerField(default=0, null=True)),
                ('blok_2', models.IntegerField(default=0, null=True)),
                ('Jami', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
            ],
            options={
                'verbose_name': '1-kurslar Yanvar',
                'verbose_name_plural': '1-kurslar Yanvar ',
            },
        ),
    ]
