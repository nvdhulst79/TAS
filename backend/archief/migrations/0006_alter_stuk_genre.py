# Generated by Django 4.0.4 on 2022-04-11 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archief', '0005_stuk_jaar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuk',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='archief.genre'),
        ),
    ]
