# Generated by Django 3.0 on 2023-11-02 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("oc_lettings_site", "0002_auto_20231102_0158"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Letting",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("title", models.CharField(max_length=256)),
                        (
                            "address",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="oc_lettings_site.Address",
                            ),
                        ),
                    ],
                    options={
                        "db_table": "oc_lettings_site_letting",
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
