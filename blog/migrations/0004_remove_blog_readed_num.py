# Generated by Django 2.0 on 2019-04-13 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190413_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
    ]
