# Generated by Django 4.2 on 2024-07-24 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                ("title", models.CharField(max_length=400)),
                ("description", models.CharField(max_length=600)),
                (
                    "instructions",
                    djrichtextfield.models.RichTextField(max_length=12000),
                ),
                (
                    "ingrendients",
                    djrichtextfield.models.RichTextField(max_length=12000),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=80,
                        scale=None,
                        size=[350, None],
                        upload_to="recipes/",
                    ),
                ),
                ("image_alt", models.CharField(max_length=200)),
                (
                    "cocktail_type",
                    models.CharField(
                        choices=[
                            ("sweet", "Sweet"),
                            ("sour", "Sour"),
                            ("strong", "Strong"),
                            ("zerozero", "ZeroZero"),
                        ],
                        default="sweet",
                        max_length=100,
                    ),
                ),
                (
                    "spirit_types",
                    models.CharField(
                        choices=[
                            ("vodka", "Vodka"),
                            ("whiskey", "Whiskey"),
                            ("rum", "Rum"),
                            ("gin", "Gin"),
                            ("liquor", "Liquor"),
                        ],
                        default="gin",
                        max_length=100,
                    ),
                ),
                ("date_posted", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipe_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_posted"],
            },
        ),
    ]
