# Generated by Django 4.0.5 on 2022-07-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='current_order_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
