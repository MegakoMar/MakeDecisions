# Generated by Django 3.2.3 on 2021-05-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_question_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='count',
        ),
        migrations.AddField(
            model_name='questions',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество вопросов'),
        ),
    ]
