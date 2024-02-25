# Generated by Django 5.0.1 on 2024-02-21 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_record_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='return_date',
        ),
        migrations.AddField(
            model_name='record',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 2, 26)),
        ),
    ]
