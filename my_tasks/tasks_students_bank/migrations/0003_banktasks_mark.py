# Generated by Django 4.2.1 on 2023-05-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_students_bank', '0002_groups_remove_userdata_group_name_userdata_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktasks',
            name='mark',
            field=models.FloatField(null=True),
        ),
    ]
