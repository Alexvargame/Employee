# Generated by Django 4.1.1 on 2023-02-01 07:26

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('empls', '0018_employeetree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeetree',
            name='director',
        ),
        migrations.AddField(
            model_name='employeetree',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='empls.employeetree', verbose_name='Начальник'),
        ),
    ]