# Generated by Django 4.1.1 on 2023-02-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0019_remove_employeetree_director_employeetree_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('главный', 'главный'), ('помощник главного', 'помощник главного'), ('старший сотрудник', 'старший сотрудник'), ('сотрудник', 'сотрудник'), ('младший сотрудник', 'младший сотрудник'), ('Стажер', 'Стажер')], max_length=20, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employeesearch',
            name='position',
            field=models.CharField(blank=True, choices=[('главный', 'главный'), ('помощник главного', 'помощник главного'), ('старший сотрудник', 'старший сотрудник'), ('сотрудник', 'сотрудник'), ('младший сотрудник', 'младший сотрудник'), ('Стажер', 'Стажер')], max_length=20, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employeetree',
            name='position',
            field=models.CharField(choices=[('главный', 'главный'), ('помощник главного', 'помощник главного'), ('старший сотрудник', 'старший сотрудник'), ('сотрудник', 'сотрудник'), ('младший сотрудник', 'младший сотрудник'), ('Стажер', 'Стажер')], max_length=20, verbose_name='Должность'),
        ),
    ]
