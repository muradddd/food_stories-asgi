# Generated by Django 3.0.1 on 2020-02-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_story_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover',
            field=models.ImageField(upload_to='cover/', verbose_name='Cover photo'),
        ),
    ]
