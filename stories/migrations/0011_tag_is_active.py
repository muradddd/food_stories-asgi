# Generated by Django 3.0.1 on 2020-01-20 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0010_auto_20200118_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=0, verbose_name='Active'),
        ),
    ]