# Generated by Django 4.2 on 2023-05-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1992-04-26'),
            preserve_default=False,
        ),
    ]
