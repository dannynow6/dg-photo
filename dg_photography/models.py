from django.db import models

# dg_photography App Models


class Photo(models.Model):
    TYPES_CHOICES = [
        ("LS", "Landscape"),
        ("SP", "Street"),
        ("MP", "Macro"),
        ("AP", "Astrophotography"),
        ("PT", "Portrait"),
        ("NP", "Night"),
        ("BW", "Black & White"),
        ("TP", "Travel"),
        ("AS", "Abstract"),
        ("EP", "Experimental"),
        ("FP", "Fashion"),
        ("LE", "Long Exposure"),
        ("AL", "Aerial"),
    ]

    FORMAT_CHOICES = [
        ("FF", "Full-Frame"),
        ("MF", "Medium-Format"),
        ("AC", "APS-C"),
        ("FT", "Micro Four Thirds"),
        ("OF", "One-Inch"),
    ]

    type = models.CharField(max_length=2, choices=TYPES_CHOICES)
    location_city = models.CharField(max_length=125, blank=True)
    location_country = models.CharField(max_length=125, blank=True)
    title = models.CharField(max_length=125)
    camera_make = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=100)
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES)
    description = models.CharField(max_length=250, blank=True)
    year_taken = models.DateField(auto_now_add=True)
    lens_make = models.CharField(max_length=125, blank=True)
    lens_model = models.CharField(max_length=125, blank=True)
    focal_length = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        """return a string representation of model"""
        title = self.title.title()
        geo = self.location_country.title()
        id = self.id
        camera = self.camera_make.title()
        return f"ID: {id} | {title} | Shot with {camera} | country: {geo}"
