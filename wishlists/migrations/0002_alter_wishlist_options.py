# Generated by Django 4.1.4 on 2022-12-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="wishlist",
            options={"verbose_name_plural": "위시리스트"},
        ),
    ]
