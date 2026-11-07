import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from django.utils.text import slugify
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

                image_ref = f"characters/images/{slugify(name)}.jpg"
                image_path = csv_path.parents[1] / "static" / image_ref

                Character.objects.update_or_create(
                    name=name,
                    defaults={
                        "description": row["description"].strip(),
                        "powers": row["powers"].strip(),
                        "category": row.get("category", "").strip() or None,
                        "image_ref": image_ref if image_path.is_file() else None,
                    }
                )

                count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Processed {count} Marvel characters"
            )
        )