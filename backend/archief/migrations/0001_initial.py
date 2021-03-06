# Generated by Django 4.0.3 on 2022-03-15 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deelname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(blank=True, max_length=50)),
                ('bijzonderheden', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Functie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=20)),
                ('omschrijving', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Persoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lidnummer', models.IntegerField(blank=True)),
                ('voornaam', models.CharField(blank=True, max_length=50)),
                ('tussenvoegsel', models.CharField(blank=True, max_length=10)),
                ('achternaam', models.CharField(max_length=50)),
                ('geslacht', models.CharField(choices=[('M', 'Man'), ('V', 'Vrouw'), ('O', 'Onbekend')], default='O', max_length=1)),
                ('geboortedatum', models.DateField(blank=True)),
                ('overleden', models.BooleanField(default=False)),
                ('lidsinds', models.DateField(blank=True)),
                ('lidtot', models.DateField(blank=True)),
                ('publicatiewens', models.CharField(choices=[('O', 'Niet zichtbaar'), ('N', 'Alleen naam'), ('A', 'Alles')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Stuk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('auteur', models.CharField(blank=True, max_length=100)),
                ('samenvatting', models.TextField(blank=True)),
                ('beschrijving', models.TextField(blank=True)),
                ('bijzonderheden', models.TextField(blank=True)),
                ('auteur_persoon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='archief.persoon')),
                ('deelnemers', models.ManyToManyField(related_name='stukken', through='archief.Deelname', to='archief.persoon')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archief.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Uitvoering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateTimeField()),
                ('lokatie', models.CharField(max_length=50)),
                ('bijzonderheden', models.TextField()),
                ('stuk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archief.stuk')),
            ],
        ),
        migrations.AddField(
            model_name='deelname',
            name='functie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archief.functie'),
        ),
        migrations.AddField(
            model_name='deelname',
            name='persoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archief.persoon'),
        ),
        migrations.AddField(
            model_name='deelname',
            name='stuk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archief.stuk'),
        ),
    ]
