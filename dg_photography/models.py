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
        ("OF", "Other Format"),
    ]

    type = models.CharField(max_length=2, choices=TYPES_CHOICES)
    location = models.CharField(max_length=125, blank=True)
    name = models.CharField(max_length=125)
    camera_make = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=100)
    format = models.CharField(max_length=2, choices=FORMAT_CHOICES)
