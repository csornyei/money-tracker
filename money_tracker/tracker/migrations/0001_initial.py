# Generated by Django 3.1.6 on 2021-02-03 19:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 2, 3, 19, 44, 0, 579324, tzinfo=utc))),
            ],
        ),
    ]
