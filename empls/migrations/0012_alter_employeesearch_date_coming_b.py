# Generated by Django 4.1.1 on 2023-01-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0011_alter_employeesearch_date_coming_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesearch',
            name='date_coming_b',
            field=models.DateField(verbose_name='Дата приема от'),
        ),
    ]