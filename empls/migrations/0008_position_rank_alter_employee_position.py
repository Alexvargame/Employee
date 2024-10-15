# Generated by Django 4.1.1 on 2023-01-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0007_rename_is_directorname_employee_is_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='rank',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ранг'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=20, verbose_name='Должность'),
        ),
    ]