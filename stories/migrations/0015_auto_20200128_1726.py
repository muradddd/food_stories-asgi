# Generated by Django 3.0.1 on 2020-01-28 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_auto_20200128_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='story',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
        migrations.DeleteModel(
            name='Append',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
