# Generated by Django 4.0.5 on 2022-07-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('view_statistics', 'Can view statistics')], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]