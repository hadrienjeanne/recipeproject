# Generated by Django 4.2.2 on 2023-06-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="picture",
            field=models.ImageField(
                default="ingredients/default.jpg", upload_to="ingredients"
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="picture",
            field=models.ImageField(default="recipes/default.jpg", upload_to="recipes"),
        ),
    ]
