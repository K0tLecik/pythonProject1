# Generated by Django 4.1.12 on 2023-11-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_position_remove_person_month_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='owner',
            field=models.IntegerField(default=1),
        ),
    ]
