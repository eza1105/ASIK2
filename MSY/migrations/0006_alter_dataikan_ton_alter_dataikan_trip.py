# Generated by Django 4.1.2 on 2022-12-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MSY", "0005_alter_dataikan_tahun"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataikan", name="ton", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="dataikan", name="trip", field=models.IntegerField(null=True),
        ),
    ]
