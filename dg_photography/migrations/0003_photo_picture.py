# Generated by Django 4.1.5 on 2023-01-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dg_photography', '0002_alter_photo_year_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
