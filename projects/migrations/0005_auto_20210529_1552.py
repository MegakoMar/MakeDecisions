# Generated by Django 3.2.3 on 2021-05-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_question_projects_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='projectId',
        ),
        migrations.AddField(
            model_name='answers',
            name='rating',
            field=models.IntegerField(null=True, verbose_name='Общая оценка решения'),
        ),
    ]