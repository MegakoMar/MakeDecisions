# Generated by Django 3.2.3 on 2021-05-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210530_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='projectId',
            field=models.IntegerField(blank=True, default=0, verbose_name='ID проекта'),
        ),
        migrations.AddField(
            model_name='questions',
            name='projectId',
            field=models.IntegerField(blank=True, default=0, verbose_name='ID проекта'),
        ),
    ]
