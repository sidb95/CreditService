# Generated by Django 5.0.6 on 2024-06-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Welcome', '0003_savedstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedstate',
            name='sid',
            field=models.IntegerField(default=1),
        ),
    ]