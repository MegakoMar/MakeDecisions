# Generated by Django 3.2.3 on 2021-05-30 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20210530_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Список ответов', 'verbose_name_plural': 'Списки ответов'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'Список вопросов', 'verbose_name_plural': 'Списки вопросов'},
        ),
    ]
