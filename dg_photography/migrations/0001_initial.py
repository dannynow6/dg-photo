# Generated by Django 4.1.5 on 2023-01-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LS', 'Landscape'), ('SP', 'Street'), ('MP', 'Macro'), ('AP', 'Astrophotography'), ('PT', 'Portrait'), ('NP', 'Night'), ('BW', 'Black & White'), ('TP', 'Travel'), ('AS', 'Abstract'), ('EP', 'Experimental'), ('FP', 'Fashion'), ('LE', 'Long Exposure'), ('AL', 'Aerial')], max_length=2)),
                ('location_city', models.CharField(blank=True, max_length=125)),
                ('location_country', models.CharField(blank=True, max_length=125)),
                ('title', models.CharField(max_length=125)),
                ('camera_make', models.CharField(max_length=100)),
                ('camera_model', models.CharField(max_length=100)),
                ('format', models.CharField(choices=[('FF', 'Full-Frame'), ('MF', 'Medium-Format'), ('AC', 'APS-C'), ('FT', 'Micro Four Thirds'), ('OF', 'One-Inch')], max_length=2)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('year_taken', models.DateField(auto_now_add=True)),
                ('lens_make', models.CharField(blank=True, max_length=125)),
                ('lens_model', models.CharField(blank=True, max_length=125)),
                ('focal_length', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]