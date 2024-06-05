# Generated by Django 5.0.6 on 2024-06-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0003_dblicense_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dblicense',
            name='data_address',
            field=models.CharField(blank=True, max_length=1099, verbose_name='Данные о смене адреса'),
        ),
        migrations.AlterField(
            model_name='dblicense',
            name='form_number_start',
            field=models.CharField(blank=True, max_length=2099, verbose_name='Основание дата возобновления'),
        ),
        migrations.AlterField(
            model_name='dblicense',
            name='form_number_stop',
            field=models.CharField(blank=True, max_length=2099, verbose_name='Основание дата прекращения'),
        ),
        migrations.AlterField(
            model_name='dblicense',
            name='form_number_suspended',
            field=models.CharField(blank=True, max_length=2099, verbose_name='Основание срок приостанавления'),
        ),
        migrations.AlterField(
            model_name='dblicense',
            name='issuing_license',
            field=models.CharField(blank=True, max_length=1099, verbose_name='Основание выдачи'),
        ),
        migrations.AlterField(
            model_name='dblicense',
            name='number_register',
            field=models.CharField(blank=True, max_length=999, unique=True, verbose_name='Номер регистрации'),
        ),
    ]
