# Generated by Django 5.0.6 on 2024-06-16 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0008_rename_isactivate_listing_isactive"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing",
            old_name="isActive",
            new_name="isActivate",
        ),
    ]
