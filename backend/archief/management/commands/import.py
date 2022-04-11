from email.mime import image
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.utils.text import get_valid_filename
from archief.models import Stuk, Afbeelding
from django.conf import settings
import os, re
from termcolor import colored
import colorama

class Command(BaseCommand):
    help = 'Importeert afbeeldingen uit de Import map. Gebruik <jaar>_<type afbeelding>_<titel>.<extensie> voor de bestandsnamen.'

    def handle(self, *args, **options):

        colorama.init()

        for bestand in os.listdir(os.path.realpath(settings.IMPORT_ROOT)):
            self.stdout.write('> ' + get_valid_filename(bestand))

            # Pak het jaar, type en titel uit de bestandsnaam
            match = re.search("^(\d{4})_([^_]+)_(.*)\.([^\.]+)$", bestand)
            if(match is None): 
                self.stdout.write(colored('  Ongeldig naam patroon', 'red'))
                continue

            jaar = match.group(1)
            type = match.group(2)
            titel = match.group(3)
            extensie = match.group(4)

            # Check of het een geldige extensie is, zoals in de settings vastgelegd
            if extensie not in settings.IMPORT_EXTENSIONS:
                self.stdout.write(colored('  Ongeldige extensie', 'red'))
                continue

            # Check of het type geldig is
            # TODO: ook accepteren obv beschrijving, case-insensitive e.d.
            if not type.upper() in dict(Afbeelding.AFBEELDING_CHOICES):
                self.stdout.write(colored(f'  Ongeldig type: {type}', 'red'))
                continue


            # Check of we deze afbeelding al hebben
            importafb = False
            try:
                bestaand = Afbeelding.objects.get(image = get_valid_filename(bestand))
                self.stdout.write(f'{bestaand}')
            except Afbeelding.DoesNotExist:
                self.stdout.write(colored('  bestaat nog niet, importeren..', 'green'))
                importafb = True

            if not importafb: continue

            # Bestaat het stuk al?
            try:
                stuk = Stuk.objects.get(titel = titel, jaar = jaar)
            except Stuk.DoesNotExist:
                stuk = Stuk(titel = titel, jaar = jaar, intevoeren = True)
                stuk.save()

            # In ieder geval de afbeelding zetten bij het stuk
            with open(os.path.join(os.path.realpath(settings.IMPORT_ROOT),  bestand), 'rb') as file:
                nieuweAfbeelding = Afbeelding(stuk = stuk, type = type) 
                nieuweAfbeelding.image.save(get_valid_filename(bestand), ImageFile(file), save = True)
