# Generated by Django 3.2.3 on 2021-05-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20210530_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question10',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 10'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question2',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 2'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question3',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 3'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question4',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 4'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question5',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 5'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question6',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 6'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question7',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 7'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question8',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 8'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question9',
            field=models.TextField(blank=True, null=True, verbose_name='Вопрос 9'),
        ),
    ]