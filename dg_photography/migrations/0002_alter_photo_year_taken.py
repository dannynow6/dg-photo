# Generated by Django 4.1.5 on 2023-01-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dg_photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='year_taken',
            field=models.DateField(blank=True),
        ),
    ]
