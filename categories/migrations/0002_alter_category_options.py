# Generated by Django 4.1.4 on 2022-12-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "카테고리"},
        ),
    ]
