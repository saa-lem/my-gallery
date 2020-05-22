from django.db import models

# Create your models here.

class ImageCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_imagecategory(self):
        self.save()



@classmethod
def search_image(cls, search_term):
    images = cls.objects.filter(image_category__name=search_term)
    return images