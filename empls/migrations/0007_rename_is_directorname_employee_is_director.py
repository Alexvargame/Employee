# Generated by Django 4.1.1 on 2023-01-19 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0006_alter_employee_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='is_directorname',
            new_name='is_director',
        ),
    ]
