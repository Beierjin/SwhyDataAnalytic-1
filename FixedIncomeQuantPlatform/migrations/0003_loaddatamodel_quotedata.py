# Generated by Django 2.0 on 2018-02-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixedIncomeQuantPlatform', '0002_auto_20180208_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='loaddatamodel',
            name='quoteData',
            field=models.TextField(default='--', verbose_name='债券序列数据'),
        ),
    ]