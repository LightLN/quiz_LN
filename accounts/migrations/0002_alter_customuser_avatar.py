# Generated by Django 4.0.5 on 2022-07-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]
