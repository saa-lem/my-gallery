from django.db import models

# Create your models here.

class ImageCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_imagecategory(self):
        self.save()



class ImagePost(models.Model):
    my_image = models.ImageField(
        upload_to='album/', default='album/default.jpg')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    image_category = models.ForeignKey(
        'ImageCategory', on_delete=models.CASCADE)
    image_location = models.ForeignKey(ImageLocation, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name

    def save_imagepost(self):
        self.save()

    def delete_imagepost(self):
        self.delete()

    def get_image_by_id(id):
        image = ImagePost.objects.get(pk=id)
        return image

    def recently_uploaded(self):
        return self.created_on >= timezone.now() + datetime.timedelta(days=1)

@classmethod
def search_image(cls, search_term):
    images = cls.objects.filter(image_category__name=search_term)
    return images