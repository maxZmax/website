# Generated by Django 3.2.3 on 2021-06-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banip',
            name='count_logo',
            field=models.IntegerField(default=0, verbose_name='Число запросов  логотипа'),
        ),
        migrations.AddField(
            model_name='banip',
            name='count_page',
            field=models.IntegerField(default=0, verbose_name='Число запросов страниц'),
        ),
    ]