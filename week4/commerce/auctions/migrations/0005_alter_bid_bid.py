# Generated by Django 5.0.6 on 2024-06-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_bid_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid",
            field=models.FloatField(default=0),
        ),
    ]
