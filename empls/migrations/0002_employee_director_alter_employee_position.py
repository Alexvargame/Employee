# Generated by Django 4.1.1 on 2023-01-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='director',
            field=models.CharField(default=2, max_length=50, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=20, verbose_name='Должность'),
        ),
    ]
