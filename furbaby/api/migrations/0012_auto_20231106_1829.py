# Generated by Django 4.0 on 2023-11-06 18:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_remove_pets_pictures_remove_users_profile_picture_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE api_users ADD CONSTRAINT valid_age_check CHECK (date_of_birth < (current_date - interval '16' year));"
        )
    ]