# Generated by Django 4.2.4 on 2023-08-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', to='tasks.tag'),
        ),
    ]