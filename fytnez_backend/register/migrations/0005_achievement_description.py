# Generated by Django 4.2.1 on 2023-08-23 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0004_alter_achievement_delete_at_alter_user_delete_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="achievement",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
