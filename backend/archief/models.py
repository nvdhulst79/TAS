from pdb import post_mortem
from django.db import models
from django.conf import settings

# Create your models here.


# Genre van een stuk
class Genre(models.Model):
    class Meta:
        verbose_name_plural = "genres"
        
    naam = models.CharField(max_length=20)
    omschrijving = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.naam

#Functie (wat doet iemand bij een stuk?)
class Functie(models.Model):
    class Meta:
        verbose_name_plural = "functies"

    naam = models.CharField(max_length=50)

    def __str__(self):
        return self.naam

# Persoon
class Persoon(models.Model):
    class Meta:
        verbose_name_plural = "personen"

    lidnummer = models.IntegerField(blank=True, null=True)
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

# Stuk, de hoofdentiteit van het archief
class Stuk (models.Model):
    class Meta:
        verbose_name_plural = "stukken"

    titel = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100, blank=True)
    auteur_persoon = models.ForeignKey(Persoon, blank=True, null=True, on_delete=models.PROTECT)
    jaar = models.IntegerField(blank=True, null=True)
    samenvatting = models.TextField(blank=True)
    beschrijving = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.PROTECT)
    deelnemers = models.ManyToManyField(
        Persoon,
        through='Deelname',
        related_name='stukken'
    )

    bijzonderheden = models.TextField(blank = True)

    intevoeren = models.BooleanField(default=False)

    def get_Jaar(self):
        return max(uitvoering.datum for uitvoering in self.uitvoering_set.all()).year

    def save(self, *args, **kwargs):
        if self.jaar is None:
            self.jaar = self.get_Jaar()
        super(Stuk, self).save(*args, **kwargs)

    def __str__(self):
        return self.titel

class Afbeelding (models.Model):
    class Meta:
        verbose_name_plural = "afbeeldingen"

    stuk = models.ForeignKey(Stuk, on_delete=models.CASCADE)

    AANKONDIGING_VOORKANT = 'AV'
    AANKONDIGING_ACHTERKANT = 'AA'
    FLYER = 'FL'
    POSTER = 'P'
    FOTO = 'F'
    AFBEELDING_CHOICES = [
        (AANKONDIGING_VOORKANT, 'Aankondiging voorkant'),
        (AANKONDIGING_ACHTERKANT, 'Aankondiging achterkant'),
        (FLYER, 'Flyer'),
        (POSTER, 'Poster'),
        (FOTO, 'Foto')
    ]
    type = models.CharField(
        max_length=2,
        choices=AFBEELDING_CHOICES,
        default=FOTO,
    )

    breedte = models.IntegerField(blank = True, null = True)
    hoogte = models.IntegerField(blank = True, null = True)

    image = models.ImageField(height_field = 'hoogte', width_field = 'breedte')



# Koppelt een persoon aan een stuk en legt vast wat die daar deed
# Koppelklasse voor Stuk.deelnemers
class Deelname(models.Model):
    class Meta:
        verbose_name_plural = "deelnames"

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
    class Meta:
        verbose_name_plural = "uitvoeringen"

    stuk = models.ForeignKey(Stuk, on_delete=models.CASCADE)
    datum = models.DateTimeField()
    lokatie = models.CharField(max_length=50)
    bijzonderheden = models.TextField()

    def __str__(self):
        return f'{self.stuk} ({self.datum:%Y-%m-%d %H:%M})'