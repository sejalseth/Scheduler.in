# Generated by Django 2.2.5 on 2019-09-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20190907_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='id',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='task_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False),
        ),
    ]