import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from characters.models import Character


class Command(BaseCommand):
    help = "Import Marvel characters from CSV"

    def handle(self, *args, **options):
        csv_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "marvel_characters.csv"
        )

        count = 0

        with csv_path.open(
            encoding="utf-8-sig",
            newline=""
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"].strip()

                if not name:
                    continue

                Character.objects.update_or_create(
                    name=name,
                    defaults={
                        "description": row["description"].strip(),
                        "powers": row["powers"].strip(),
                    }
                )

                count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Processed {count} Marvel characters"
            )
        )