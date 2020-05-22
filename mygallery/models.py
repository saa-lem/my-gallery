from django.db import models

# Create your models here.

@classmethod
def search_image(cls, search_term):
    images = cls.objects.filter(image_category__name=search_term)
    return images