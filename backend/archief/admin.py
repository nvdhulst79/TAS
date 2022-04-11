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
    fields = ('image', 'thumbnail', 'type', 'breedte', 'hoogte')
    readonly_fields = ('breedte', 'hoogte', 'thumbnail')
    extra = 0

    def thumbnail(self, obj):
        from django.utils.html import format_html

        if obj.image:
            return format_html('<img src="%s"  height="100px"/>' % obj.image.url)
        else:
            return 'No_image'
    
    thumbnail.short_descriptions = 'Thumbnail'

class DeelnameInline(admin.StackedInline):
    model = Deelname
    extra = 0

class UitvoeringInline(admin.StackedInline):
    model = Uitvoering
    extra = 0

@admin.register(Stuk)
class StukAdmin(admin.ModelAdmin):
    model = Stuk
    list_display = ('titel', 'jaar')
    inlines = [
        AfbeeldingInline,
        DeelnameInline,
        UitvoeringInline
    ]
    fields = ('titel', 'jaar', 'auteur', 'auteur_persoon', 'samenvatting', 'beschrijving', 'genre', 'bijzonderheden')
