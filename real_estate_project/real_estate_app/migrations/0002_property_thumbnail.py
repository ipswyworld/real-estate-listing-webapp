# Generated by Django 4.2.14 on 2024-08-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("real_estate_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
        ),
    ]
