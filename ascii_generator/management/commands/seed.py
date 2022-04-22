from django.core.management.base import BaseCommand
from ascii_generator.models import Letter
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
# MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
# MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    # def add_arguments(self, parser):
    #     parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')

        run_seed()

        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""

    logging.debug("Clearing database...")
    Letter.objects.all().delete()


def run_seed():
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

                        logging.debug(f"Added '{letter}' to database")
                    except:
                        logging.warning(
                            f"Failed to add '{letter}' to database"
                        )

                # gets the second half of the line, without the quotes
                # e.g. 33 '!' -> !
                letter = line.split(" ", 1)[-1].strip()[1:-1]

                # reset the representation string
                representation = ""
                continue

            representation += f"{line.strip()}|"
