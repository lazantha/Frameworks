# Generated by Django 4.2.3 on 2023-09-04 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_members_member'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]