# Generated by Django 4.0 on 2021-12-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0003_player_ballsize_player_shoesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='BallSize',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='ShoeSize',
            field=models.IntegerField(default=False),
        ),
    ]
