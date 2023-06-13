# Generated by Django 4.2.1 on 2023-06-03 13:04

from django.db import migrations, models
import fytnez_backend.register.validators.user_validator


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0001_create_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(
                validators=[
                    fytnez_backend.register.validators.user_validator.UserValidator.validate_bithday
                ]
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="height",
            field=models.IntegerField(
                validators=[
                    fytnez_backend.register.validators.user_validator.UserValidator.validate_not_zero
                ]
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="weight",
            field=models.IntegerField(
                validators=[
                    fytnez_backend.register.validators.user_validator.UserValidator.validate_not_zero
                ]
            ),
        ),
    ]
