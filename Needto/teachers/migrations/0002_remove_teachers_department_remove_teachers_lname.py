# Generated by Django 4.1.4 on 2022-12-30 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='department',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='lname',
        ),
    ]
