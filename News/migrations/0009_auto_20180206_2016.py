# Generated by Django 2.0.1 on 2018-02-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0008_auto_20180206_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publications',
            name='author',
        ),
        migrations.AddField(
            model_name='publications',
            name='author',
            field=models.ManyToManyField(to='News.Authors'),
        ),
    ]