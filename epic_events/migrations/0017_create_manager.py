from datetime import date

from django.db import migrations

from epic_events.models.collaborator import Collaborator
from epic_events.models.department import Department


def create_manager(apps, schema_editor):
    department = Department(name="Gestion")
    department.save()

    manager = Collaborator(
        first_name="Ahlem",
        last_name="Chateur",
        email="AhlemStotar@gmail.com",
        birthdate=date(year=1994, month=1, day=28),
        department=department,
    )
    manager.save()
    manager.set_password("00000000pW-")
    manager.save()


class Migration(migrations.Migration):
    dependencies = [
        ("epic_events", "0016_alter_collaborator_birthdate"),
    ]

    operations = [migrations.RunPython(create_manager)]
