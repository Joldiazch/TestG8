# Generated by Django 3.1.5 on 2021-01-21 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20210121_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eps',
            old_name='name',
            new_name='eps_name',
        ),
        migrations.RenameField(
            model_name='rol',
            old_name='name',
            new_name='rol_name',
        ),
    ]
