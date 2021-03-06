# Generated by Django 3.0.4 on 2020-04-09 18:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('status', models.BooleanField(default='False')),
                ('roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentData')),
            ],
        ),
    ]
