# Generated by Django 4.2.4 on 2024-11-14 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0038_remove_goodsmodel_latitude_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="goodsmodel",
            name="latitude",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="goodsmodel",
            name="longitude",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="goodsmodel",
            name="stocked_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="goods",
                to="store.stockedimage",
            ),
        ),
    ]
