# Generated by Django 4.1.1 on 2023-01-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0013_alter_employee_date_coming_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_coming',
            field=models.DateField(verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='employeesearch',
            name='date_coming_b',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='employeesearch',
            name='date_coming_e',
            field=models.DateField(),
        ),
    ]
