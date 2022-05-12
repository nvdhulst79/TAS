import graphene
from graphene_django import DjangoObjectType

from archief import models

class GenreType(DjangoObjectType):
    class Meta:
        model = models.Genre

class FunctieType(DjangoObjectType):
    class Meta:
        model = models.Functie

class PersoonType(DjangoObjectType):
    class Meta:
        model = models.Persoon

class StukType(DjangoObjectType):
    class Meta:
        model = models.Stuk

class DeelnameType(DjangoObjectType):
    class Meta:
        model = models.Deelname

class UitvoeringType(DjangoObjectType):
    class Meta:
        model = models.Uitvoering

class AfbeeldingGQLType(DjangoObjectType):
    class Meta:
        model = models.Afbeelding


class Query(graphene.ObjectType):
    alle_stukken = graphene.List(StukType)
    persoon_op_lidnummer = graphene.Field(PersoonType, lidnummer = graphene.String())

    def resolve_alle_stukken(root, info):
        return (
            models.Stuk.objects
            .all()
        )

    def resolve_persoon_op_lidnummer(root, info, lidnummer):
        return (
            models.Persoon.objects
            .select_related("stukken")
            .get(lidnummer=lidnummer)
        )

schema = graphene.Schema(query = Query)