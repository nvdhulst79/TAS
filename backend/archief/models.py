from multiprocessing import managers
from django.db import models
from django.conf import settings

# Create your models here.


# Genre van een stuk
class Genre(models.Model):
    naam = models.CharField(max_length=20)
    omschrijving = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.naam

#Functie (wat doet iemand bij een stuk?)
class Functie(models.Model):
    naam = models.CharField(max_length=50)

    def __str__(self):
        return self.naam

# Persoon
class Persoon(models.Model):
    lidnummer = models.IntegerField(blank=True)
    voornaam = models.CharField(max_length=50, blank=True)
    tussenvoegsel = models.CharField(max_length=10, blank=True)
    achternaam = models.CharField(max_length=50)

    MAN = 'M'
    VROUW = 'V'
    ONBEKEND = 'O'
    GESLACHT_CHOICES = [
        (MAN, 'Man'),
        (VROUW, 'Vrouw'),
        (ONBEKEND, 'Onbekend'),
    ]
    geslacht = models.CharField(
        max_length=1,
        choices=GESLACHT_CHOICES,
        default=ONBEKEND,
    )

    geboortedatum = models.DateField(blank=True, null=True)
    overleden = models.BooleanField(default=False)

    lidsinds = models.DateField(blank=True, null=True)
    lidtot = models.DateField(blank=True, null=True)

    # TODO: alternatieve namen
    # TODO: foto

    NIETZICHTBAAR = 'O'
    ALLEENNAAM = 'N'
    ALLES = 'A'
    PUBLICATIE_CHOICES = [
        (NIETZICHTBAAR, 'Niet zichtbaar'),
        (ALLEENNAAM, 'Alleen naam'),
        (ALLES, 'Alles'),
    ]
    publicatiewens = models.CharField(
        max_length=1,
        choices=PUBLICATIE_CHOICES,
        default=ALLEENNAAM
    )

    def VolledigeNaam(self):
        return f'{self.achternaam}, {self.voornaam} {self.tussenvoegsel} '.strip().replace('  ', ' ')

    def __str__(self):
        return self.VolledigeNaam()

# Stuk, de hoofdeintiteit van het archief
class Stuk (models.Model):
    titel = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100, blank=True)
    auteur_persoon = models.ForeignKey(Persoon, blank=True, null=True, on_delete=models.PROTECT)
    samenvatting = models.TextField(blank=True)
    beschrijving = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    deelnemers = models.ManyToManyField(
        Persoon,
        through='Deelname',
        related_name='stukken'
    )

    bijzonderheden = models.TextField(blank = True)
    
    #TODO aankondiging afbeelding(en)
    #TODO overige afbeeldingen

    def BepaalJaar(self):
        pass

    def __str__(self):
        return self.titel

# Koppelt een persoon aan een stuk en legt vast wat die daar deed
# Koppelklasse voor Stuk.deelnemers
class Deelname(models.Model):
    stuk = models.ForeignKey(Stuk, on_delete=models.CASCADE)
    persoon = models.ForeignKey(Persoon, on_delete=models.PROTECT)
    functie = models.ForeignKey(Functie, on_delete=models.PROTECT)
    rol = models.CharField(max_length=50, blank=True)
    bijzonderheden = models.TextField(blank=True)
    # TODO: sortering

    def __str__(self):
        return f'{self.stuk}, {self.functie}: {self.persoon}'

# Uitvoeringen van een stuk (datum en lokatie)
class Uitvoering(models.Model):
    stuk = models.ForeignKey(Stuk, on_delete=models.CASCADE)
    datum = models.DateTimeField()
    lokatie = models.CharField(max_length=50)
    bijzonderheden = models.TextField()

    def __str__(self):
        return f'{self.stuk} ({self.datum:%Y-%m-%d %H:%M})'