# Generated by Django 4.0 on 2021-12-23 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='UserID',
            new_name='UserId',
        ),
    ]