# Generated by Django 3.2.9 on 2021-11-10 14:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Хитрое JSON поле')),
            ],
            options={
                'db_table': 'mymodel',
            },
        ),
    ]
