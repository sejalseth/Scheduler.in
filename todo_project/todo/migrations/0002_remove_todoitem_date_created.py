# Generated by Django 2.2.5 on 2019-09-07 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='date_created',
        ),
    ]
