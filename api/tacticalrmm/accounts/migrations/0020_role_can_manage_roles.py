# Generated by Django 3.2.1 on 2021-05-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='can_manage_roles',
            field=models.BooleanField(default=False),
        ),
    ]
