from django.contrib import admin
from archief.models import Genre, Functie, Persoon, Stuk, Deelname, Uitvoering

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

@admin.register(Stuk)
class StukAdmin(admin.ModelAdmin):
    model = Stuk

@admin.register(Deelname)
class DeelnameAdmin(admin.ModelAdmin):
    model = Deelname

@admin.register(Uitvoering)
class UitvoeringAdmin(admin.ModelAdmin):
    model = Uitvoering