# Generated by Django 4.2.3 on 2023-09-25 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_posttable_id_posttable_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttable',
            name='category',
        ),
        migrations.RemoveField(
            model_name='posttable',
            name='link',
        ),
    ]
