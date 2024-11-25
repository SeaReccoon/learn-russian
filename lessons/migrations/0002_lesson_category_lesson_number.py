# Generated by Django 5.1.3 on 2024-11-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер занятия'),
        ),
    ]