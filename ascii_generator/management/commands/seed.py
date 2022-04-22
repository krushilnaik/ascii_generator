from django.core.management.base import BaseCommand
from ascii_generator.models import Letter
from pathlib import Path

from util.custom_logging import debug, info, warning


class Command(BaseCommand):
    def handle(self, *args, **options):
        info('Seeding database...')

        run_seed()

        info('Done.')


def clear_data():
    """Deletes all the table data"""

    info("Clearing database...")
    Letter.objects.all().delete()


def run_seed():
    """Seed the database"""
    clear_data()

    ALPHABET_FILE = Path(__file__).parent / "alphabet.txt"

    with open(ALPHABET_FILE, encoding="utf-8") as alphabet:
        letter = ""
        representation = ""

        for line in alphabet:
            if line[0].isdigit():
                if letter != "":
                    # add the freshly-built letter to the database
                    try:
                        temp = Letter(
                            letter=letter,

                            # [:-1] gets rid of the trailing "|"
                            representation=representation[:-1]
                        )

                        temp.save()

                        debug(f"Added '{letter}' to database")
                    except:
                        warning(f"Failed to add '{letter}' to database")

                # gets the second half of the line, without the quotes
                # e.g. 33 '!' -> !
                letter = line.split(" ", 1)[-1].strip()[1:-1]

                # reset the representation string
                representation = ""
                continue

            representation += f"{line.strip()}|"
