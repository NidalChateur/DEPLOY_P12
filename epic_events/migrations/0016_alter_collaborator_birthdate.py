# Generated by Django 5.0.1 on 2024-01-09 06:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("epic_events", "0015_alter_event_contract_alter_event_support_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collaborator",
            name="birthdate",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Date de naissance"
            ),
            preserve_default=False,
        ),
    ]
