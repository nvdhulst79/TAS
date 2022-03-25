from email.mime import image
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.utils.text import get_valid_filename
from archief.models import Stuk, Afbeelding
from backend.settings import IMPORT_ROOT, BASE_DIR, IMPORT_EXTENSIONS
import os, re
from termcolor import colored

class Command(BaseCommand):
    help = 'Importeert afbeeldingen uit de Import map. Gebruik <jaar>_<type afbeelding>_<titel>.<extensie> voor de bestandsnamen.'

    def handle(self, *args, **options):

        for bestand in os.listdir(os.path.realpath(IMPORT_ROOT)):
            self.stdout.write('> ' + get_valid_filename(bestand))

            match = re.search("^(\d{4})_([^_]+)_(.*)\.([^\.]+)$", bestand)

            if(match is None): 
                self.stdout.write(colored('  Ongeldig naam patroon', 'red'))
                continue

            jaar = match.group(1)
            type = match.group(2)
            titel = match.group(3)
            extensie = match.group(4)

            if extensie not in IMPORT_EXTENSIONS:
                self.stdout.write(colored('  Ongeldige extensie', 'red'))
                continue

            bestaand = Afbeelding.objects.get(image = get_valid_filename(bestand))
            self.stdout.write(f'{bestaand}')