from django.contrib import admin
from archief.models import Genre, Functie, Persoon, Stuk, Deelname, Uitvoering, Afbeelding

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre

@admin.register(Functie)
class FunctieAdmin(admin.ModelAdmin):
    model = Functie

@admin.register(Persoon)
class PersoonAdmin(admin.ModelAdmin):
    model = Persoon

class AfbeeldingInline(admin.TabularInline):
    model = Afbeelding
    fields = ('image', 'type', 'breedte', 'hoogte')
    readonly_fields = ('breedte', 'hoogte')
    extra = 0

class DeelnameInline(admin.StackedInline):
    model = Deelname
    extra = 0

class UitvoeringInline(admin.StackedInline):
    model = Uitvoering
    extra = 0

@admin.register(Stuk)
class StukAdmin(admin.ModelAdmin):
    model = Stuk
    inlines = [
        AfbeeldingInline,
        DeelnameInline,
        UitvoeringInline
    ]
    fields = ('titel', 'auteur', 'auteur_persoon', 'samenvatting', 'beschrijving', 'genre', 'bijzonderheden')