# Generated by Django 4.1.4 on 2022-12-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.URLField(blank=True, verbose_name="프로필 사진"),
        ),
    ]
