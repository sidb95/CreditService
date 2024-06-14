# Generated by Django 5.0.6 on 2024-06-13 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Welcome', '0004_savedstate_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('bill_date', models.DateField()),
                ('principal_due', models.IntegerField(default=0)),
                ('min_due', models.IntegerField(default=0)),
                ('term', models.IntegerField(default=1)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Welcome.loan')),
            ],
        ),
    ]