# Generated by Django 4.2.4 on 2024-01-12 16:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("like", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="like",
            options={"verbose_name": "like", "verbose_name_plural": "likes"},
        ),
    ]