# Generated by Django 3.2.3 on 2021-05-22 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(default='change-me', unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('upload_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['upload_date'],
            },
        ),
    ]
