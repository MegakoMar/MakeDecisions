# Generated by Django 3.2.3 on 2021-05-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_projects_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество вопросов'),
        ),
    ]