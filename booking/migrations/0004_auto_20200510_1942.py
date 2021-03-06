# Generated by Django 3.0.6 on 2020-05-10 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200510_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingavailability',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=1800), help_text='Meeting duration, used for creating booking slots.'),
        ),
        migrations.AlterField(
            model_name='bookingavailability',
            name='padding',
            field=models.DurationField(default=datetime.timedelta(seconds=300), help_text='Minimum allowed amount of time between 2 meetings.'),
        ),
    ]
