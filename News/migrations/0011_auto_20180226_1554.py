# Generated by Django 2.0.1 on 2018-02-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_auto_20180226_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='author',
            field=models.ManyToManyField(help_text='Выберите авторов', to='News.Authors'),
        ),
    ]
