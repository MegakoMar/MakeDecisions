# Generated by Django 3.2.3 on 2021-05-29 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210529_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='question',
            new_name='questions',
        ),
    ]
