# Generated by Django 2.2.5 on 2019-09-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todoitem_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]