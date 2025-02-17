# Generated by Django 4.2.4 on 2025-02-06 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0042_alter_goodsmodel_stocked_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoreBanner",
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
                ("image", models.ImageField(upload_to="media/store_banner/")),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="banner",
                        to="store.storemodel",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Store Banner",
                "db_table": "store_banner",
            },
        ),
    ]
