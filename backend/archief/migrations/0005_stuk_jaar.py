# Generated by Django 4.0.4 on 2022-04-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archief', '0004_alter_afbeelding_options_alter_deelname_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuk',
            name='jaar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
