# Generated by Django 5.0.2 on 2024-02-24 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_remove_record_return_date_record_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='due_date',
            field=models.DateField(default=datetime.date(2024, 2, 29)),
        ),
    ]
