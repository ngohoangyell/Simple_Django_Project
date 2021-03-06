# Generated by Django 4.0.4 on 2022-05-24 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("WC", "Wan Chai"),
                            ("CW", "Central and Western"),
                            ("SK", "Sai Kung"),
                            ("E", "Eastern"),
                            ("S", "Southern"),
                            ("TW", "Tsuen Wan"),
                            ("N", "North"),
                            ("KC", "Kowloon City"),
                            ("YTM", "Yau Tsim Mong"),
                            ("ST", "Sha Tin"),
                            ("I", "Islands"),
                            ("YL", "Yuen Long"),
                            ("TP", "Tai Po"),
                            ("WTS", "Wong Tai Sin"),
                            ("TM", "Tuen Mun"),
                            ("KTS", "Kwai Tsing"),
                            ("SSP", "Sham Shui Po"),
                            ("KT", "Kwun Tong"),
                        ],
                        db_index=True,
                        max_length=3,
                    ),
                ),
                ("latitude", models.DecimalField(decimal_places=7, default=0, max_digits=10)),
                ("longitude", models.DecimalField(decimal_places=7, default=0, max_digits=10)),
                ("name", models.TextField(null=True)),
            ],
            options={
                "verbose_name": "hybeta_location",
                "verbose_name_plural": "hybeta_locations",
                "db_table": "hybeta_location",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("phone", models.CharField(default="", max_length=20, null=True)),
                ("category", models.CharField(choices=[("GP", "General Practitioner"), ("D", "Dentistry"), ("C", "Cardiology"), ("F", "Family"), ("K", "Kid")], max_length=20)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("available_time", models.TextField(null=True)),
                ("location", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="jobs.location")),
            ],
            options={
                "verbose_name": "hybeta_doctor",
                "verbose_name_plural": "hybeta_doctors",
                "db_table": "hybeta_doctor",
                "ordering": ["-id"],
                "index_together": {("category", "price")},
            },
        ),
        migrations.CreateModel(
            name="DoctorTranslation",
            fields=[
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("language_code", models.CharField(choices=[("EN", "English"), ("HK", "Hong Kong")], max_length=20)),
                ("name", models.CharField(default="", max_length=255)),
                ("note", models.TextField(null=True)),
                ("doctor", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="doctor_translations", to="jobs.doctor")),
            ],
            options={
                "verbose_name": "hybeta_doctor_translation",
                "verbose_name_plural": "hybeta_doctor_translations",
                "db_table": "hybeta_doctor_translation",
                "ordering": ["-id"],
                "index_together": {("doctor", "language_code")},
            },
        ),
    ]
