# Generated by Django 4.0.4 on 2022-04-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archief', '0006_alter_stuk_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuk',
            name='intevoeren',
            field=models.BooleanField(default=False),
        ),
    ]
