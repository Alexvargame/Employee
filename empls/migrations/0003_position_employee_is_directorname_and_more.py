# Generated by Django 4.1.1 on 2023-01-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0002_employee_director_alter_employee_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='is_directorname',
            field=models.BooleanField(default=False, verbose_name='Есть подчиненные'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='director',
            field=models.CharField(max_length=50, verbose_name='Начальник'),
        ),
    ]