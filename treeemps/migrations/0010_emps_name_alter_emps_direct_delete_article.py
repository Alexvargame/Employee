# Generated by Django 4.1.1 on 2023-02-20 06:12

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('treeemps', '0009_alter_subs_name_alter_subs_parent_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='emps',
            name='name',
            field=models.CharField(choices=[('Иван Иванович', 'Иван Иванович'), ('Мария', 'Мария'), ('Олег', 'Олег'), ('Сергей', 'Сергей'), ('Ольга', 'Ольга'), ('Марина', 'Марина'), ('Владимир', 'Владимир'), ('Наталья', 'Наталья'), ('Илья', 'Илья'), ('Анна', 'Анна'), ('Света', 'Света'), ('Евгений', 'Евгений'), ('Оксана', 'Оксана'), ('Антон', 'Антон'), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', ''), ('', '')], default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emps',
            name='direct',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='treeemps.subs'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
