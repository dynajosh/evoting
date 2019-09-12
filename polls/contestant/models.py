from django.db import models
from django.conf import settings
from django.db.models import Q
# Create your models here.




class Contestant(models.Model):
    CATEGORIES = (
        ("President", "President"),
        ("Vice President", "Vice President"),
        ("General Secretary", "General Secretary"),
        ("Assistant General Secretary", "Assistant General Secretary"),
        ("Treasurer", "Treasurer"),
        ("Financial Secretary", "Financial Secretary"),
        ("Librarian", "Librarian"),
        ("Sports Director", "Sports Director"),
        ("P.R.O", "P.R.O"),
        ("Null", "Null")
    )

    name = models.CharField(max_length = 120)
    level = models.CharField(max_length = 120)
    votes = models.PositiveIntegerField(default=0)
    reg_number = models.CharField(max_length = 120)
    category = models.CharField(max_length = 120, choices = CATEGORIES, default='Null')
    image = models.ImageField(upload_to='image/', blank=True, null=True)