# Generated by Django 5.0.6 on 2024-06-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_bid_alter_listing_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid",
            field=models.IntegerField(default=0),
        ),
    ]
