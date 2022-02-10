# Generated by Django 3.2.3 on 2021-07-11 11:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

from .. import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.LAST_SEEN_SITE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LastActive",
            fields=[
                (
                    "id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("module", models.CharField(default=settings.LAST_SEEN_DEFAULT_MODULE, max_length=20)),
                (
                    "last_active",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.LAST_SEEN_SITE_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-last_active",),
                "unique_together": {("user", "site", "module")},
            },
        ),
    ]
