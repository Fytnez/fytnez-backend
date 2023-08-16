# Generated by Django 4.2.1 on 2023-08-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0002_user_create_at_user_delete_at_user_total_points_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("delete_at", models.DateTimeField()),
                ("name", models.CharField(max_length=255)),
                ("points", models.IntegerField()),
                ("is_secret", models.BooleanField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("WATER_CONSUMPTION", "Water Consumption"),
                            ("WORKOUT", "Workout"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        help_text="\n        Coloque a constante do icon do Angular de acordo com o seguinte site:\n        https://api.flutter.dev/flutter/material/Icons-class.html#constants\n    ",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
